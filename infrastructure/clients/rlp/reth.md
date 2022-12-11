`root/crates/common/`
  `rlp/`
        `decode.rs`
            - 500 loc
              - About %50 of the file is tests
              - Same file for testing and logic
            - `Header`
              - Pretty raw way of decoding rlp
            - Uses `macro_rules!`, nice!
              - Simplifies the implementation fro various types
            - 
        `encode.rs`
            - 600 loc
              - 50% + is tests
            - Pretty clean, uses again macro rules to simply the code
        