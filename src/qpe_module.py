from qiskit import QuantumCircuit, Aer, execute
from .qft_module import apply_qft
import numpy as np

def qpe_circuit(unitary: QuantumCircuit, eigenstate: QuantumCircuit, n_count: int) -> QuantumCircuit:
    """
    Constructs a Quantum Phase Estimation (QPE) circuit.

    Parameters:
        unitary (QuantumCircuit): Unitary operator (must be controlled in implementation)
        eigenstate (QuantumCircuit): State that is an eigenstate of the unitary
        n_count (int): Number of counting qubits

    Returns:
        QuantumCircuit: Complete QPE circuit
    """
    eigen_qubits = eigenstate.num_qubits
    total_qubits = n_count + eigen_qubits
    circuit = QuantumCircuit(total_qubits, n_count)

    circuit.h(range(n_count))
    circuit.compose(eigenstate, qubits=range(n_count, total_qubits), inplace=True)

    for i in range(n_count):
        repetitions = 2 ** i
        controlled_unitary = unitary.control()
        for _ in range(repetitions):
            circuit.compose(controlled_unitary, qubits=[i] + list(range(n_count, total_qubits)), inplace=True)

    inverse_qft = QuantumCircuit(n_count)
    apply_qft(inverse_qft, list(range(n_count)))
    circuit.compose(inverse_qft.inverse(), qubits=range(n_count), inplace=True)
    circuit.measure(range(n_count), range(n_count))

    return circuit

def simulate_qpe(circuit: QuantumCircuit) -> dict:
    """
    Executes a given QPE circuit on a simulator and prints the phase estimation.

    Parameters:
        circuit (QuantumCircuit): Fully assembled QPE circuit

    Returns:
        dict: Measurement outcomes
    """
    backend = Aer.get_backend('aer_simulator')
    job = execute(circuit, backend=backend, shots=1024)
    result = job.result()
    counts = result.get_counts()

    print("Quantum Phase Estimation Result Summary")
    print("----------------------------------------")
    for outcome, frequency in sorted(counts.items(), key=lambda x: -x[1]):
        reversed_bin = outcome[::-1]
        decimal_value = int(reversed_bin, 2)
        estimated_phase = decimal_value / (2 ** circuit.num_clbits)
        print(f"Observed: {outcome} | Phase: {estimated_phase:.6f} | Frequency: {frequency}")
    
    return counts

