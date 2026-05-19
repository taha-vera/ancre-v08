# ANCRE v0.8 — Artifact (PETS 2027)

## Structure
ancre-v08/
├── src/main.rs
├── benchmarks/
│   ├── petseval.py
│   └── vera_radio_demo.py
├── Dockerfile
├── Cargo.toml
└── README_artifact.md

## Quick Start
python3 benchmarks/petseval.py --runs 100 --epsilon 0.5

## Docker
docker build -t ancre-v08 .
docker run --env PYTHONHASHSEED=42 ancre-v08

## Rust Tests
cargo test
# Expected: 59 passed; 0 failed

## Artifact Claims
1. Full Rust implementation included
2. All evaluation scripts runnable in 1 command
3. Self-contained, no external datasets needed

## Expected Output
Station         Baseline    ANCRE       MSE        rho
FIP             0.6357      0.6383   6.8e-06      0.940
France Inter    0.6422      0.6605   3.4e-04      0.910
France Culture  0.6577      0.7089   2.6e-03      0.890
France Musique  0.6769      0.7229   2.1e-03      0.880
Mouv            0.6425      0.6614   3.6e-04      0.920
France Info     0.6527      0.6446   6.6e-05      0.930

## Privacy Guarantee
epsilon=0.5-DP, delta=0
Honest-but-curious model (H6)
