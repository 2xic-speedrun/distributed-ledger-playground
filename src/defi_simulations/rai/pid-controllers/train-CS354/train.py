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


    def method(self, new_speed):
        if self.current_distance <= self.goal_distance:
            # add some real friction !!!
            friction = random.randint(3, 100) / 100
            new_speed = new_speed(self) * friction

            old_speed = self.speed
            for _ in range(100):
                distance_moved = 1/2 * (new_speed * friction + old_speed ) * (1/100)
                self.current_distance += distance_moved
            self.speed = old_speed
            return False
        return True

