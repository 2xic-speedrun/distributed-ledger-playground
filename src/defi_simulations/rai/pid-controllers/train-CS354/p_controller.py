from train import Train

def p_control(train: Train):
    k_p = 5
    e = train.goal_distance - train.current_distance

    return k_p * e

