Welcome to the **QUBO Calculator**, a deeply engineered repository that merges theoretical elegance with hands-on quantum computing. Designed for professional demonstrations, academic competitions, and cryptographic disruption, this project showcases mastery over some of the most advanced quantum algorithms in contemporary computation.

> This is not a hobbyist demo. This is a command center for simulating quantum supremacy over classical boundaries.

---

## 🧠 Project Philosophy

In an era where classical computation begins to falter under exponential complexity, quantum computing emerges not just as a tool — but as a paradigm shift. This repository embraces that shift, and presents a **multi-algorithmic arsenal**:

- Factoring large integers using **Shor’s Algorithm** to challenge RSA encryption.
- Precise phase extraction with **Quantum Phase Estimation** (QPE).
- Custom construction of the **Quantum Fourier Transform** (QFT) — the backbone of quantum signal analysis.
- Solving discrete binary optimization problems via **QUBO** formulation using **QAOA**.

Whether you’re simulating quantum attacks on encryption or optimizing NP-hard problems, this repo is built to **execute, analyze, and awe**.

---

## 🧬 Core Quantum Systems Implemented

### 1. **Shor's Algorithm**
Factorizes a composite number \( N \in \mathbb{Z}^+ \) using quantum period finding and classical post-processing:
```python
factor_integer(21)
# Output: [3, 7]
```
Used to demonstrate the cryptographic vulnerability of RSA-based security.

### 2. **Quantum Fourier Transform (QFT)**
Builds and applies an n-qubit QFT:
```python
circuit = create_qft_circuit(3)
circuit.draw()
```
QFT is the core of many quantum protocols — this implementation is exact and swappable into larger algorithms.

### 3. **Quantum Phase Estimation (QPE)**
Estimates the eigenphase \( \phi \) of a unitary operator \( U \) applied to an eigenvector \( |\psi\rangle \):
```python
qc = qpe_circuit(unitary, eigenstate, 4)
simulate_qpe(qc)
```
Crucial for chemistry, HHL, and beyond.

### 4. **QUBO Solver with QAOA**
Solves binary quadratic optimization problems like Max-Cut, graph coloring, etc.:
```python
simple_qubo_problem()
# Returns optimal bitstring and cost
```

---

## 🧪 File & Folder Structure

```
qubo-calculator/
├── src/                        # Core algorithm modules
│   ├── __init__.py
│   ├── shor_algorithm.py       # Full Shor’s algorithm implementation
│   ├── qft_module.py           # Quantum Fourier Transform logic
│   ├── qpe_module.py           # Quantum Phase Estimation framework
│   └── qubo_solver.py          # QUBO model solved using QAOA
│
├── main.py                    # Unified CLI runner
├── requirements.txt           # Dependencies
├── .gitignore                 # Clean Git commits
├── LICENSE                    # MIT License
└── notebooks/
    └── demo_playground.ipynb  # Interactive demonstration notebook
```

---

## 🔧 Installation & Setup

```bash
git clone https://github.com/yourusername/qubo-calculator.git
cd qubo-calculator
pip install -r requirements.txt
python main.py
```

Use `notebooks/demo_playground.ipynb` to explore the algorithms visually.

---

## 🚀 Usage Highlights

### Run Everything from `main.py`
```bash
python main.py
```
This will:
- Factorize 21 using Shor’s algorithm
- Build and display a QFT on 3 qubits
- Estimate a quantum phase with 4 counting qubits
- Solve a small QUBO via QAOA

Each module runs independently as well. Perfect for integrating into larger research setups.

---

## 📚 Concepts Covered in Depth
- Modular Arithmetic and Periodicity
- Quantum Parallelism
- Controlled Phase Operations
- QFT Unitarity and Eigen Decomposition
- Binary Optimization Formulations
- Hybrid Classical-Quantum Algorithms
- Entanglement, Superposition, and Circuit Interference

---

## 🧠 Ideal For:
- Quantum Cryptography Competitions
- Post-Quantum Security Demonstrations
- Optimization Research
- Teaching Advanced Quantum Algorithms
- Benchmarking Qiskit Implementations

---
