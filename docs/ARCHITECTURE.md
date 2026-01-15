# Architecture Overview

This document describes the **public showcase architecture**
of the Architecture Irreversibility Model.

It explains structure and mechanics without exposing
operational or commercial details.

---

## Design Goals

- Mechanical clarity over completeness
- Reproducibility with minimal dependencies
- Clear separation between research and operations
- No client, calibration, or monetization logic

---

## High-Level Structure

src/
├─ model/ # Core node and system mechanics
├─ graph/ # Dependency graphs and propagation
└─ simulation/ # Monte Carlo simulation drivers


The architecture mirrors the conceptual model:
nodes → dependencies → dynamics → statistics.

---

## Core Components

### Node
Represents a bounded subsystem that:
- accumulates stress,
- compensates via capacity,
- and crosses an irreversibility threshold.

### System
A container coordinating multiple nodes
over a simulation horizon.

### Dependency Graph
A directed weighted graph describing
how stress propagates between subsystems.

### Simulation
Monte Carlo estimation of:
- probability of irreversibility,
- expected economic loss,
- cascade-driven amplification.

---

## Intentional Omissions

The following are **intentionally absent**:
- questionnaire ingestion
- parameter calibration pipelines
- commercial artifacts
- client-specific workflows

These belong to a private workbench.

---

## Boundary Statement

This repository demonstrates **how the model works**,
not **how it is applied commercially**.

The separation is deliberate and enforced.
