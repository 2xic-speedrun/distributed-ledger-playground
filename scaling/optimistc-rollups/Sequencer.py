from L1 import Layer1
from L2 import Layer2

class Sequencer:
    def __init__(self, l1: Layer1, l2: Layer2) -> None:
        self.l1 = l1
        self.l2 = l2

    def process(self):
        while len(self.l1.queue):
            self.l2.deposits.append(self.l1.queue.pop())
