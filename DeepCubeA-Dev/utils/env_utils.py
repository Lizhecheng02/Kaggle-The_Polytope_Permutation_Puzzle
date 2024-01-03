import re
import math
from environments.environment_abstract import Environment
import numpy as np

TOTAL = ['cube_2/2/2', 'cube_3/3/3', 'cube_4/4/4', 'cube_5/5/5',
       'cube_6/6/6', 'cube_7/7/7', 'cube_8/8/8', 'cube_9/9/9',
       'cube_10/10/10', 'cube_19/19/19', 'cube_33/33/33', 'wreath_6/6',
       'wreath_7/7', 'wreath_12/12', 'wreath_21/21', 'wreath_33/33',
       'wreath_100/100', 'globe_1/8', 'globe_1/16', 'globe_2/6',
       'globe_3/4', 'globe_6/4', 'globe_6/8', 'globe_6/10', 'globe_3/33',
       'globe_8/25']

def get_environment(env_name: str, args) -> Environment:
    env_name = env_name.lower()
    puzzle_n_regex = re.search("puzzle(\d+)", env_name)
    env: Environment

    if env_name == 'cube3':
        from environments.cube3 import Cube3
        env = Cube3()
    elif puzzle_n_regex is not None:
        from environments.n_puzzle import NPuzzle
        puzzle_dim: int = int(math.sqrt(int(puzzle_n_regex.group(1)) + 1))
        env = NPuzzle(puzzle_dim)
    elif 'lightsout' in env_name:
        from environments.lights_out import LightsOut
        m = re.search('lightsout([\d]+)', env_name)
        env = LightsOut(int(m.group(1)))
    elif env_name == 'sokoban':
        from environments.sokoban import Sokoban
        env = Sokoban(10, 4)
    elif env_name == 'santa':
        from environments.santa import Santa
        import pickle
        
        load_path = "/home/xuanming/kaggle/santa/allowed_moves.pickle"
        with open(load_path, 'rb') as f:
            allowed_moves = pickle.load(f)
        load_path = "/home/xuanming/kaggle/santa/inverse_allowed_moves.pickle"
        with open(load_path, 'rb') as f:
            inverse_allowed_moves = pickle.load(f)
        
        goal= np.array(['A', 'A', 'A', 'A', 'A','A','A','A','A','B', 'B', 'B', 'B','B','B', 'B','B','B','C', 'C', 'C', 'C','C','C', 'C','C','C','D',
       'D', 'D', 'D', 'D','D','D', 'D','D','E', 'E', 'E', 'E','E','E','E','E','E', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F'])
        env = Santa(goal, allowed_moves['cube_3/3/3'], inverse_allowed_moves['cube_3/3/3'])
    elif env_name in TOTAL:
        from environments.santa_new import Santa
        import pickle
        
        load_path = "./allowed_moves.pickle"
        with open(load_path, 'rb') as f:
            allowed_moves = pickle.load(f)
        load_path = "./inverse_allowed_moves.pickle"
        with open(load_path, 'rb') as f:
            inverse_allowed_moves = pickle.load(f)
        load_path = "./num_class.pickle"
        with open(load_path, 'rb') as f:
            num_class = pickle.load(f)
        load_path = "./num_tiles.pickle"
        with open(load_path, 'rb') as f:
            num_tiles = pickle.load(f)        
        load_path = "./goal_states.pickle"
        with open(load_path, 'rb') as f:
            goal_states = pickle.load(f)        
        env = Santa(num_tiles[env_name], num_class[env_name], allowed_moves[env_name], inverse_allowed_moves[env_name], goal_states[env_name], False)
    else:
        raise ValueError('No known environment %s' % env_name)

    return env
