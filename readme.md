# DeFi simulator

The plan is to create simulators fro various DeFi environment. The core will be written in rust, but have python interface. This should allow various scientific use cases.

It's also is a nice way for me to get a good idea how theses protocols actually work. 
```
What I cannot build. I do not understand.

― Richard Feynman
```

----

We want to have a simulator for most of DeFi, but some of the project that we want to have simulator for to start with

## Lending

- [Aave](https://raw.githubusercontent.com/aave/aave-protocol/master/docs/Aave_Protocol_Whitepaper_v1_0.pdf).
- [Compound](https://compound.finance/documents/Compound.Whitepaper.pdf)

## AMM
- [Curve](https://curve.fi/files/crypto-pools-paper.pdf)
- [Uniswap v2 / v3](https://uniswap.org/whitepaper.pdf)
- [SNX Atomic Exchange](https://sips.synthetix.io/sips/sip-120/)

### Stablecoins
- [Aave GHO stablecoin](https://governance.aave.com/t/introducing-gho/8730)
- [Rai](https://raw.githubusercontent.com/reflexer-labs/whitepapers/master/English/rai-english.pdf)
- [DAI](https://makerdao.com/whitepaper/White%20Paper%20-The%20Maker%20Protocol_%20MakerDAO%E2%80%99s%20Multi-Collateral%20Dai%20(MCD)%20System-FINAL-%20021720.pdf)
- [FRAX](https://docs.frax.finance/overview)

### Options
- [https://www.opyn.co/](https://www.opyn.co/)
- [https://perp.com/](https://perp.com/)

### MEV
- we will also investigate how MEV can affect some of theses dapps. https://www.mev.wiki/

---
There are also ideas closely connected to DeFi worth creating simulators for. For instance seigniorage shares is something used by successfully for some stablecoins, and less so for others.

[Seigniorage Shares](https://blog.bitmex.com/wp-content/uploads/2018/06/A-Note-on-Cryptocurrency-Stabilisation-Seigniorage-Shares.pdf)

