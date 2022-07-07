

class Rai:
    def __init__(self) -> None:
        # this was supposedly the initial value when rai was launched
        # used for redemption / liquidations etc
        self.internal_value = 3.14
        # changed based on market conditions
        self.redemption_rate = 0 

    def tick(self, market_price):
        """
            measure difference between market_price and internal price
                - i.e uniswap
            PID controller should adjust redemption rate
                is market price higher than internal ? 
                    - positive rate
                is market price below internal ? 
                    - negative rate
            This again changes the internal value
            This again changes the market price.
        """
        pass

