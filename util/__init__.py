from app import TRAINING_NAME

#X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X+X
# logging
#:.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:

def logger_name(name):
    return f'{TRAINING_NAME}.{name}'

def parse_log_args(str):
    return [conf.strip() for conf in str.split(',')]
