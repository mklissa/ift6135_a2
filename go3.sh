#!/usr/bin/bash



name="hyper_transformer_drop" 

tmux new-session -d -s $name



tmux new-window -t $name: -n "0"
tmux send-keys -t $name: "bash"
tmux send-keys -t $name:  Enter
tmux send-keys -t $name: "source activate assign2"
tmux send-keys -t $name:  Enter
tmux send-keys -t $name: "python3 ptb-lm.py --model=TRANSFORMER --optimizer=SGD_LR_SCHEDULE --initial_lr=20 --batch_size=128 --seq_len=35 --hidden_size=512 --num_layers=6 --dp_keep_prob=0.9"
tmux send-keys -t $name:  Enter

tmux new-window -t $name: -n "1"
tmux send-keys -t $name: "bash"
tmux send-keys -t $name:  Enter
tmux send-keys -t $name: "source activate assign2"
tmux send-keys -t $name:  Enter
tmux send-keys -t $name: "python3 ptb-lm.py --model=TRANSFORMER --optimizer=SGD_LR_SCHEDULE --initial_lr=30 --batch_size=128 --seq_len=35 --hidden_size=512 --num_layers=6 --dp_keep_prob=0.9"
tmux send-keys -t $name:  Enter

tmux new-window -t $name: -n "2"
tmux send-keys -t $name: "bash"
tmux send-keys -t $name:  Enter
tmux send-keys -t $name: "source activate assign2"
tmux send-keys -t $name:  Enter
tmux send-keys -t $name: "python3 ptb-lm.py --model=TRANSFORMER --optimizer=SGD_LR_SCHEDULE --initial_lr=40 --batch_size=128 --seq_len=35 --hidden_size=512 --num_layers=6 --dp_keep_prob=0.9"
tmux send-keys -t $name:  Enter


tmux -2 attach-session -t $name
