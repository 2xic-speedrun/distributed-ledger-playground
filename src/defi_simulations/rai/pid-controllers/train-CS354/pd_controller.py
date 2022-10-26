from train import Train

def pd_control(train: Train):
    k_p = 5
    k_d = 2

    e = train.goal_distance - train.current_distance

    if train.state['e_error'] is None:
        train.state['e_error'] = e

    de_dt = (e - train.state['e_error']) / train.dt

    change = k_p * e + k_d * de_dt

    train.state['e_error'] = de_dt

    return change
    