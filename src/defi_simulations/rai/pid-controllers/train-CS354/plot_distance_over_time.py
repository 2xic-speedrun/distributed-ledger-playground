from p_controller import p_control
from pd_controller import pd_control
from pid_controller import pid_control
from open_control import open_control
from main import test_method
import matplotlib.pyplot as plt

if __name__ == "__main__":
    plt.plot(test_method(open_control).results_distance_over_time, label="Open control")
    plt.plot(test_method(p_control).results_distance_over_time, label="p control")
    plt.plot(test_method(pd_control).results_distance_over_time, label="pd control")
    plt.plot(test_method(pid_control).results_distance_over_time, label="pid control")
    plt.legend(loc="upper left")
    plt.xlabel("Time")
    plt.ylabel("Distance")
    plt.savefig("distance_over_time.png")
