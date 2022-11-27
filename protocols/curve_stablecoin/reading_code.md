## Some notes when reading the code
Code at commit : b9394d4c50d7fc99baacddd42d677bdd4c83a897

- AMM
  - One collateral token
  - One borrow token
  - _p_oracle_up
    - Complicated curve function logic
  -  exchange function 
     -  looks weird, seems to be taken out of the original curve pool logic since it uses the same index mechanism, when the amm only supports two tokens atm.
     -  But I guess that is nice to have the same interface so it's easy to add new tokens, and it's easier to deal with since it's a int and not an address one has to deal with

- Controller
  - Liquidations
    - Health factors
    - A lot of math logic here also
  - Controls the markets (AMM etc)
  - 
