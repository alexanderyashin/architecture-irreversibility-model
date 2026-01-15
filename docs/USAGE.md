# Usage Guide

This document explains how to run the **public demonstration**
of the Architecture Irreversibility Model.

The example is fully synthetic and requires no external data.

---

## Requirements

- Python 3.10+
- Standard scientific stack

Recommended:
python -m venv venv
source venv/bin/activate
pip install numpy networkx matplotlib

---

## Running the Minimal Simulation (No Cascades)


python src/simulation/run.py


This will:
- build a small synthetic system,
- run a Monte Carlo simulation,
- print probability of irreversibility and expected loss.

---

## Running the Cascade Simulation



python src/simulation/run_cascade.py


This demonstrates:
- dependency-driven stress propagation,
- non-linear escalation,
- increased expected loss under cascades.

---

## Interpreting the Output

Typical output fields:
- `p_any_cross` — probability that at least one node crosses irreversibility
- `expected_loss` — average economic loss across runs
- `avg_crossed_nodes` — average number of irreversibly crossed nodes

Values are **scenario-dependent** and illustrative only.

---

## Modifying the Example

You may experiment by changing:
- node forcing or capacity,
- thresholds,
- dependency weights.

Do **not** interpret results as predictions.
They illustrate **mechanics**, not forecasts.

---

## Disclaimer

This code is provided for research and educational purposes.
It is not a production tool and does not replace professional judgment.
