import unittest

from .sandwich_attack import SandwichAttack
from ...uniswap.uniswap_erc20 import UNISWAP_ADDRESS
from ...utils.ERC20 import ERC20
from ...uniswap.uniswap_erc20 import UniswapErc20
from .front_run_liquidity_trap_token import TrapToken


class TestFrontRunLiquidityTrapToken(unittest.TestCase):
    def setUp(self) -> None:
        self.mev_bot = 0x44
        self.user = 0x22
    
        self.uniswap_pool = UNISWAP_ADDRESS
    
        self.eth = ERC20("ETH")
        self.trap_token = TrapToken()

        self.eth.mint(1000, self.uniswap_pool)
        self.trap_token.mint(1000, self.uniswap_pool)

        self.eth.mint(
            1000,
            self.mev_bot,
        )

        self.eth.mint(
            1000,
            self.user,
        )

        self.uniswap_pool = UniswapErc20(
            self.eth,
            self.trap_token,
        )

    def test_front_run(self):
        mev_amount = 0
        # trap on, they don't receive the full amount
        mev_amount += self.uniswap_pool.swap_reserve0(self.mev_bot, 100)
        self.trap_token.incrementBlock()
        mev_amount += self.uniswap_pool.swap_reserve0(self.mev_bot, 100)
        self.trap_token.incrementBlock()
        mev_amount += self.uniswap_pool.swap_reserve0(self.mev_bot, 100)
        self.trap_token.incrementBlock()

        # no more trap
        self.uniswap_pool.swap_reserve0(self.user, 100)

        assert self.trap_token.balances[self.mev_bot] < self.trap_token.balances[self.user]

