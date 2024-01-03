from typing import List, Dict, Tuple, Union
import numpy as np
from torch import nn
from random import randrange

from utils.pytorch_models import ResnetModel
from .environment_abstract import Environment, State


class SantaState(State):
    __slots__ = ['state','num_wildcards','hash', 'goal_state']

    def __init__(self, state: np.ndarray, num_wildcards: int= 0, goal_state = None):
        self.state = state
        self.num_wildcards = num_wildcards
        self.hash = None
        self.goal_state = goal_state

    def __hash__(self):
        if self.hash is None:
            self.hash = hash(self.state.tostring())
        return self.hash

    def __eq__(self, other):
        return (self.state != other.state).sum() <= self.num_wildcards


class Santa(Environment):

    def __init__(self, goal_state, allowed_moves, inverse_allowed_moves):
        super().__init__()

        # self.goal_state = goal_state
        self.goal_state = np.arange(0, len(goal_state), 1)

        self.allowed_moves = allowed_moves
        self.allowed_moves_idxs = {i: a for i, a in enumerate(allowed_moves.keys())}
        self.inverse_allowed_moves = inverse_allowed_moves

    def next_state(self, states: List[SantaState], action: str) -> Tuple[List[SantaState], List[float]]:
        states_np = np.stack([x.state for x in states], axis=0)
        states_next_np, transition_costs = self._move_np(states_np, action)
        num_wildcards = [x.num_wildcards for x in states]
        states_next: List[SantaState] = [SantaState(x, y) for x, y in zip(list(states_next_np), num_wildcards)]

        return states_next, transition_costs

    def prev_state(self, states: List[SantaState], action: str) -> List[SantaState]:
        states_np = np.stack([x.state for x in states], axis=0)
        states_next_np = self._prev_np(states_np, action)
        num_wildcards = [x.num_wildcards for x in states]
        
        states_prev: List[SantaState] = [SantaState(x, y) for x, y in zip(list(states_next_np), num_wildcards)]

        return states_prev

    def generate_goal_states(self, num_states: int, np_format: bool = False) -> Union[List[SantaState], np.ndarray]:
        if np_format:
            goal_np: np.ndarray = np.expand_dims(self.goal_state.copy(), 0)
            solved_states: np.ndarray = np.repeat(goal_np, num_states, axis=0)
        else:
            solved_states: List[SantaState] = [SantaState(self.goal_state.copy(), 0) for _ in range(num_states)]

        return solved_states

    def is_solved(self, states: List[SantaState]) -> np.ndarray:
        states_np = np.stack([state.state for state in states], axis=0)
        goal_states_np = [state.goal_state for state in states if state.goal_state is not None]
        if len(goal_states_np) > 0:
            res = []
            for state in states:
                if (state.state != state.goal_state).sum() <= state.num_wildcards:
                    res.append(True)
                else:
                    res.append(False)
            return np.array(res)
        else:    
            is_equal = np.equal(states_np, np.expand_dims(self.goal_state, 0))

            return np.all(is_equal, axis=1)
    
        # if state in states:
        #     if (state.state != self.goal_state).sum() <= state.num_wildcards:
        #         continue
        #     else:
        #         return False
        # return True

    def state_to_nnet_input(self, states: List[SantaState]) -> List[np.ndarray]:
        states_np = np.stack([state.state for state in states], axis=0)

        representation_np: np.ndarray = states_np // (len(self.goal_state) // 6)
        # representation_np: np.ndarray = representation_np.astype(self.dtype)

        representation: List[np.ndarray] = [representation_np]

        return representation

    def get_num_moves(self) -> int:
        return len(self.allowed_moves)

    def get_nnet_model(self) -> nn.Module:
        print(len(self.goal_state))
        nnet = ResnetModel(len(self.goal_state), 6, 5000, 1000, 4, 1, True)

        return nnet

    def generate_states(self, num_states: int, backwards_range: Tuple[int, int]) -> Tuple[List[SantaState], List[int]]:
        assert (num_states > 0)
        assert (backwards_range[0] >= 0)
        assert self.fixed_actions, "Environments without fixed actions must implement their own method"

        # Initialize
        scrambs: List[int] = list(range(backwards_range[0], backwards_range[1] + 1))
        num_env_moves: int = self.get_num_moves()

        # Get goal states
        states_np: np.ndarray = self.generate_goal_states(num_states, np_format=True)

        # Scrambles
        scramble_nums: np.array = np.random.choice(scrambs, num_states)
        num_back_moves: np.array = np.zeros(num_states)

        # Go backward from goal state
        moves_lt = num_back_moves < scramble_nums
        while np.any(moves_lt):
            idxs: np.ndarray = np.where(moves_lt)[0]
            subset_size: int = int(max(len(idxs) / num_env_moves, 1))
            idxs: np.ndarray = np.random.choice(idxs, subset_size)

            move: int = randrange(num_env_moves)
            
            states_np[idxs], _ = self._move_np(states_np[idxs], self.allowed_moves_idxs[move])

            num_back_moves[idxs] = num_back_moves[idxs] + 1
            moves_lt[idxs] = num_back_moves[idxs] < scramble_nums[idxs]

        states: List[SantaState] = [SantaState(x) for x in list(states_np)]

        return states, scramble_nums.tolist()

    def expand(self, states: List[State]) -> Tuple[List[List[State]], List[np.ndarray]]:
        assert self.fixed_actions, "Environments without fixed actions must implement their own method"

        # initialize
        num_states: int = len(states)
        num_env_moves: int = self.get_num_moves()

        states_exp: List[List[State]] = [[] for _ in range(len(states))]

        tc: np.ndarray = np.empty([num_states, num_env_moves])

        # numpy states
        states_np: np.ndarray = np.stack([state.state for state in states])
        num_wildcards_np: np.ndarray = np.stack([state.num_wildcards for state in states])

        # for each move, get next states, transition costs, and if solved
        move_idx: int
        move: int
        for move_idx in range(num_env_moves):
            # next state
            states_next_np: np.ndarray
            tc_move: List[float]
            states_next_np, tc_move = self._move_np(states_np, self.allowed_moves_idxs[move_idx])

            # transition cost
            tc[:, move_idx] = np.array(tc_move)

            for idx in range(len(states)):
                states_exp[idx].append(SantaState(states_next_np[idx], num_wildcards_np[idx]))

        # make lists
        tc_l: List[np.ndarray] = [tc[i] for i in range(num_states)]

        return states_exp, tc_l

    def _move_np(self, states_np: np.ndarray, action: str):
        if isinstance(action, int):
            action = self.allowed_moves_idxs[action]
        states_next_np = states_np[:, self.allowed_moves[action]].copy()

        transition_costs: List[float] = [1.0 for _ in range(states_np.shape[0])]

        return states_next_np, transition_costs
    
    def _prev_np(self, states_np: np.ndarray, action: str):

        states_next_np = states_np[:, self.inverse_allowed_moves[action]].copy()

        return states_next_np
    
    