from collections import defaultdict
import random
from state import State

class Train:
    def __init__(self, initial_speed, goal_distance) -> None:
        self.speed = initial_speed
        self.current_distance = 0
        self.goal_distance = goal_distance

        self.dt = 1

        self.state =  State()
        self.results_speed_over_time = []
        self.results_distance_over_time = []

    def method(self, new_speed):
        if self.current_distance <= self.goal_distance:
            # add some real friction !!!
            friction = 0.8
            new_speed = new_speed(self) * friction
            new_speed = max(new_speed, 5)

            # and make the acceleration not constant!
            old_speed = self.speed
            self.current_distance += 1/2 * (new_speed * friction + old_speed )
            self.speed = new_speed
            self.results_speed_over_time.append(self.speed)
            self.results_distance_over_time.append(self.current_distance)

            return False
        return True

