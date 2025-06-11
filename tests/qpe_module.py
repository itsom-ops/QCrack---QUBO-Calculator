import pytest
from src.qpe_module import qpe_circuit
from qiskit.circuit.library import PhaseGate
from qiskit.quantum_info import Statevector
from qiskit import QuantumCircuit


def test_qpe_circuit_structure():
    eigenstate = QuantumCircuit(1)
    eigenstate.h(0)
    unitary = PhaseGate(0.25 * 2 * 3.1415)  # phase = pi/2
    qc = qpe_circuit(unitary, eigenstate, n_count=3)
    assert isinstance(qc, QuantumCircuit)
    assert qc.num_qubits > 1
