# Bloom Filter

- Parameters: m bits, k hashes for n items, p false positive rate.
- Formulas: m ≈ -(n ln p)/(ln 2)^2, k ≈ (m/n) ln 2.
- False positives possible; no false negatives for inserted items.
