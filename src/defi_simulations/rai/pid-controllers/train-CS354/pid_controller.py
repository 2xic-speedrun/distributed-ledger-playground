from train import Train

def pid_control(train: Train):
    k_p = 5
    k_d = 2
    k_i = 1.5

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
    