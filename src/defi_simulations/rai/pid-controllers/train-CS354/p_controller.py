from train import Train
from parameters import k_p

def p_control(train: Train):
    e = train.goal_distance - train.current_distance

    return k_p * e

