

class State:
    def __init__(self) -> None:
        self.state = {}

    def __getitem__(self, item):
        if item in self.state:
            return self.state[item]
        return None

    def __setitem__(self, key, value):
        self.state[key] = value
        