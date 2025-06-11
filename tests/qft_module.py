import pytest
from src.qft_module import create_qft_circuit
from qiskit import QuantumCircuit


def test_qft_output_qubits():
    n = 3
    qc = create_qft_circuit(n)
    assert isinstance(qc, QuantumCircuit)
    assert qc.num_qubits == n
    assert qc.depth() > 0  # Ensures some logic has been added
