from qiskit import QuantumCircuit
import numpy as np

def apply_qft(circuit: QuantumCircuit, qubits: list) -> QuantumCircuit:
    """
    Applies the Quantum Fourier Transform (QFT) in-place to specified qubits of the given circuit.

    Parameters:
        circuit (QuantumCircuit): Quantum circuit to modify
        qubits (list): List or range of qubit indices on which to apply QFT

    Returns:
        QuantumCircuit: The same circuit with QFT applied on specified qubits.
    """
    n = len(qubits)
    for i in range(n):
        circuit.h(qubits[i])
        for j in range(i + 1, n):
            angle = np.pi / (2 ** (j - i))
            circuit.cp(angle, qubits[j], qubits[i])

    for i in range(n // 2):
        circuit.swap(qubits[i], qubits[n - i - 1])

    return circuit

def create_qft_circuit(n: int) -> QuantumCircuit:
    """
    Constructs a standalone QFT circuit of n qubits.

    Parameters:
        n (int): Number of qubits

    Returns:
        QuantumCircuit: Quantum circuit with QFT applied.
    """
    circuit = QuantumCircuit(n)
    apply_qft(circuit, list(range(n)))
    return circuit

