from train import Train

def open_control(train: Train):
    return train.goal_distance - train.current_distance
