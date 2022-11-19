
class Layer1:
    def  __init__(self) -> None:
        self.queue = []

    def deposit(self, value, user):
        self.queue.append((value, user))
        