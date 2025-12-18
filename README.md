#Triangle-Free r-Regular Graphs

## Overview

This repository contains the work of **Group 6** on *Problem 5*, focusing on connected **triangle-free r-regular graphs** with **r odd**. The aim is to solve the problem **at least partially** through a combination of theoretical constraints and computational exploration.
This project studies **connected triangle-free r-regular graphs** (with **r odd**) under three increasingly weaker conditions related to **strong odd independent sets**. The goal is to **characterize**, **search**, and **experimentally explore** graphs satisfying these conditions, combining **systematic enumeration**, **randomized methods**, and **structural insights from strongly regular graphs**.

The problem naturally splits into **three different subproblems**, with logical implications:

> (i) ⇒ (ii) ⇒ (iii)

Two classical examples satisfying **(i)** are:

* the **Petersen graph**
* the complete bipartite graph **K_{r,r}**, for odd r

---

## Definitions

* **r-regular graph**: every vertex has degree r.
* **Triangle-free**: the graph contains no 3-cycles.
* **N(v)**: the open neighborhood of a vertex v.
* **Strong odd independent set**: an odd-cardinality independent set that is maximal under inclusion.
* **α_od(G)**: the maximum size of a strong odd independent set in G.

Throughout, we assume **r is odd** and **G is connected**, unless stated otherwise.

---

## Problem Statements

Let G be a connected triangle-free r-regular graph with r odd.

### (i) Universal Neighborhood Optimality

For **every vertex v**, the neighborhood N(v) is a **maximum strong odd independent set**.

### (ii) Existential Neighborhood Optimality

There exists **at least one vertex v** such that N(v) is a **maximum strong odd independent set**.

### (iii) Maximum Size Condition

The graph satisfies:

α_od(G) = r.

No additional requirement is imposed on neighborhoods in this case.

---

## Known Constraints and Observations

### Structural Restrictions

* **Diameter constraint**: A necessary condition for (i) and (ii) is

  > diam(G) ≤ 3

* **Order bound for (iii)**: For r ≥ 3 (not necessarily odd),

  > |V(G)| ≤ r(r² − 1)

### Implications

* Any graph satisfying (i) automatically satisfies (ii).
* Any graph satisfying (ii) automatically satisfies (iii).
* Conditions become strictly weaker from (i) to (iii).

---

## Project Goals

Taking the above constraints into account, this project has three main objectives.

### 1. Systematic Search (Small Order)

* Enumerate connected triangle-free r-regular graphs of **small order**.
* Test each graph against conditions **(i)**, **(ii)**, and **(iii)**.
* Record minimal examples, counterexamples, and isomorphism classes.

Tools and techniques may include:

* Graph generation with degree and girth constraints
* Isomorphism rejection
* Exact computation of α_od(G)

---

### 2. Random Walks on Larger Graphs

* Explore graphs of **larger order** with **diameter at most 3**.
* Apply random edge-switching or rewiring operations preserving:

  * r-regularity
  * triangle-freeness
  * connectivity
* Empirically test how frequently conditions (i), (ii), or (iii) occur.

This approach complements exhaustive search where enumeration becomes infeasible.

---

### 3. Strongly Regular Graphs as Candidates

The Petersen graph and K_{r,r} belong to the class of **strongly regular graphs** with parameters:

> srg(n, r, λ = 0, μ)

This motivates a focused investigation of:

* Known SRGs with λ = 0
* Their odd independence structure
* Whether additional SRGs satisfy (i), (ii), or (iii)

This direction combines **theoretical structure** with **computational verification**.

---

## Expected Outcomes

* Classification results for small r and small |V(G)|
* Identification of new examples or proof of nonexistence in certain parameter ranges
* Empirical evidence supporting or refuting conjectures on necessity/sufficiency
* Deeper understanding of the role of strong regularity and diameter constraints

---

## Notes

* All three conditions are treated as **separate but related problems**.
* Results for (i) automatically inform (ii) and (iii).
* Care should be taken to distinguish **maximum** vs **maximal** strong odd independent sets.

---

## References and Background

Relevant topics include:

* Regular triangle-free graphs
* Strongly regular graphs
* Odd independence and parity constraints
* Graph diameter and extremal bounds

