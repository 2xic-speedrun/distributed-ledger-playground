from p_controller import p_control
from pd_controller import pd_control
from pid_controller import pid_control
from open_control import open_control
from train import Train
import random

def test_method(method):
    train = Train(
        0,
        100
    )
    for _ in range(1000):
        #print(train.current_distance)
        if train.method(method):
            break
    return train


if __name__ == "__main__":
    print(open_control, test_method(open_control).current_distance)
    print(p_control, test_method(p_control).current_distance)
    print(pd_control, test_method(pd_control).current_distance)
    print(pid_control, test_method(pid_control).current_distance)

