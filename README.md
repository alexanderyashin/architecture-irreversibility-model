# Architecture Irreversibility Model

This repository provides a **research-grade, executable showcase**
of a quantitative model for architectural irreversibility in complex systems.

The model formalizes how systems accumulate stress, cross irreversible thresholds,
and incur non-linear economic loss—especially under dependency-driven cascades.

---

## What is included

- **Threshold-based node dynamics**
- **Dependency graphs and cascade propagation**
- **Monte Carlo simulation** of irreversible transitions
- **Synthetic examples** for demonstration and reproducibility

All code and data in this repository are intentionally **sanitized** and
**non-operational**. They are suitable for research, learning, and illustration.

---

## What is NOT included

- Commercial tooling or workflows  
- Client-specific data or calibration  
- Questionnaires, ingestion pipelines, or pricing logic  
- Any material enabling replication of a commercial service  

This repository is a **showcase**, not a product.

---

## Conceptual Overview

Each subsystem is modeled as a node with:
- load (forcing),
- compensation capacity,
- irreversibility threshold,
- and economic impact.

Irreversibility emerges when accumulated stress crosses thresholds.
Dependencies introduce **cascade amplification**, producing fat-tailed risk.

---

## Reproducibility

All examples are:
- synthetic,
- self-contained,
- and reproducible on a standard Python environment.

See `docs/USAGE.md` for instructions.

---

## Status

Stable research showcase.  
Public artifacts are exported from a private workbench via a strict one-way policy.

---

## Citation

If you use this work in research or teaching, please cite it.
See `CITATION.cff` for details.
