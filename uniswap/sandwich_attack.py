from .simulator import UniswapPair

class SandwichAttack:
    def __init__(self) -> None:
        self.uniswap = UniswapPair(
            10,
            10
        )

    def trade_asset_1(self, amount: float):
        self._front_run_asset1(amount)
        self.uniswap.swap_reserve0(amount)
        sell = self.uniswap.swap_reserve1(amount)
        return (sell - amount)

    def _front_run_asset1(self, amount):
        self.uniswap.swap_reserve0(amount)
