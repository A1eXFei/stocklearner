# StockLearner

## Description

Deep learning for China A share stock data

## Purpose

User machine learning to perdict stock price

## Requirements

Supervised learning:

- tensorflow >= `1.8.0`
- pandas >= `0.23.2`
- numpy >= `0.23.2`

Reinforcement learning:

- all in supervised learning
- backtrader >= `1.9.59.122`

### Install requirements

```shell
pip install -r requirements.txt
```

## Run

1. Modify `app.config` to set the training data path, eval data path and model config path
2. Create or modify your own model config ini file and put it into the model config path
3. Run `sl_ops.py` for supervised learning and run `rl_ops.py` for reinforcement learning

## Models

So far MLP and RNN(LSTM) only

### Data

Please use CSV file with columns as below:

`"DATE", "OPEN", "HIGH", "CLOSE", "LOW", "VOLUME", "PRICE_CHANGE", "P_CHANGE", "TURNOVER", "LABEL"`

- Date will be removed during training
- Or modify `/feed/csv_data.py` to support the new columns

### Known issue

- Multiprocessing has issues, so only place one model config file and train one time. This will be fixed in future

### TODO

1. Will add batch normalization in MLP soon
2. Create new config folder for config classes，rename current config folder to config_file and only store for .ini files
3. Extract train and predict ops from model classes, create new train_ops for them
4. Refactor for DQN
   1. Create config class for DQN
   2. Add double Q learning
   3. Add Duel DQN
   4. Add Prioritized Replay Buffer
   5. Add Tenorboard summary
   6. Add learning rate ops
5. Create A3C for deep reinforcement learning
6. Use eager execution to support TensorFlow2.0 in future