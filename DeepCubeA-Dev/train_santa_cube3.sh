CUDA_VISIBLE_DEVICES=0 python ctg_approx/avi.py --env santa --states_per_update 50000000 --batch_size 10000 --nnet_name santa --max_itrs 1000000 --loss_thresh 0.1 --back_max 500 --num_update_procs 30
