# ANCRE v0.8 — 3-Party MPC Protocol

Most privacy systems build guarantees on what they protect.
ANCRE builds its guarantees on what it irrevocably destroys.

## What is ANCRE v0.8?

ANCRE v0.8 is a 3-party MPC protocol achieving ε=0.5-DP
for B2B audio analytics under honest-majority assumption.

## Parties
- P1: Collector (Radio France)
- P2: DP Aggregator (VERA)
- P3: Trusted Third Party (CNIL)

## Key improvement over v0.7
| Version | Trust model | Attack required |
|---------|------------|-----------------|
| v0.7 | Trust NAV | Single server compromise |
| v0.8 | H6-MPC honest majority | Collusion of 2/3 parties |

## Status
- [ ] Protocol specification
- [ ] Formal proofs
- [ ] Implementation
- [ ] Paper

## Related
- ANCRE v0.7: github.com/taha-vera/ancre-final
- HAL preprint: pending DOI
