

"""
Users submit values to the network

With a price estimate p_i and a coin weight F

People submitting within the median wins 2xF

All others loose F

"""


from collections import UserString


class SchellingPoint:
    def __init__(self):
        self.values = {}

    def submit(self, user_id, price, value):
        self.values[user_id] = price  # [price, value]

    def reveal(self):
        values = len(self.values)
        price_submission = sorted(self.values.values())

        size = (values + 1) // 2 if values % 2 == 1 else values // 2
        q_1 = sum(price_submission[:size]) / size
        q_3 = sum(price_submission[size:]) / size

        q_2 = q_3 - q_1
        # user within q_1 and q_2 is safe

        print({
            "q_1": q_1,
            "q_2": q_2,
            "q_3": q_3
        })


if __name__ == "__main__":
    x = SchellingPoint()

    for v in range(1, 5):
        for i in range(1, 10):
            x.submit(int(f"{v}{i}"), 10 + v // 2, None)

    x.reveal()
