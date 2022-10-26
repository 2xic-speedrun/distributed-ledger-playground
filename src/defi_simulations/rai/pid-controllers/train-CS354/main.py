from p_controller import p_control
from pd_controller import pd_control
from pid_controller import pid_control
from open_control import open_control
from train import Train
import random

def test_method(method):
    print(method)
    test_train_open_loop = Train(
        0,
        100
    )
    for i in range(100):
        print(test_train_open_loop.current_distance)
        if test_train_open_loop.method(method):
            break
    print(test_train_open_loop.current_distance)


if __name__ == "__main__":
    if False:
        test_method(open_control)
        test_method(p_control)
        test_method(pd_control)
    test_method(pid_control)

