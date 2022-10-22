q96 = 2 ** 96


def value_to_q96(value):
    return int(value * q96)


class QValue:
    def __init__(self, n):
        self.n = n
        self.q = False

    def to(self):
        if self.q:
            raise Exception("Value is q")
        self.n = int(self.n * q96)
        self.q = True
        return 

    def back(self):
        if not self.q:
            raise Exception("Value is q")
        self.n = self.n // q96
        self.q = False

    @property
    def value(self):
        return round(self.n, 2)
        