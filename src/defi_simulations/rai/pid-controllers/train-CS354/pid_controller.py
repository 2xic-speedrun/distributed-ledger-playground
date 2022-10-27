from train import Train
from parameters import k_p, k_d, k_i

def pid_control(train: Train):
    e = train.goal_distance - train.current_distance

    if train.state['e_error'] is None:
        train.state['e_error'] = e
        train.state['e_sum'] = 0

    e_sum = train.state['e_sum'] + e / train.dt
    de_dt = (e - train.state['e_error'])

    change = k_p * e + k_i * e_sum + k_d * de_dt

    train.state['e_error'] = de_dt
    train.state['e_sum'] = e_sum

    return change
    