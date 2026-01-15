# Synthetic Case: How to Run

This example demonstrates the **Architecture Irreversibility Model**
on a fully synthetic system with three subsystems and directional dependencies.

The goal is to show:
- how irreversible transitions emerge,
- how cascades amplify risk,
- and how expected loss can be estimated quantitatively.

---

## Structure

- `graph.yaml`  
  Defines subsystem dependencies and stress propagation weights.

- `src/simulation/run.py`  
  Monte Carlo simulation **without cascades**.

- `src/simulation/run_cascade.py`  
  Monte Carlo simulation **with cascades**.

---

## Prerequisites

Python ≥ 3.10

Install dependencies:

```bash
pip install -r requirements.txt
