from src import factor_integer, create_qft_circuit, qpe_circuit, simulate_qpe, simple_qubo_problem
from qiskit import QuantumCircuit

def run_shor():
    print("\n--- Executing Shor's Algorithm ---")
    number = 21  # Example composite number
    factor_integer(number)

def run_qft():
    print("\n--- Generating QFT Circuit ---")
    n_qubits = 3
    circuit = create_qft_circuit(n_qubits)
    print(circuit.draw())

def run_qpe():
    print("\n--- Executing Quantum Phase Estimation ---")
    n_count = 4
    unitary = QuantumCircuit(1)
    unitary.p(2 * 3.1416 * 0.125, 0)
    eigenstate = QuantumCircuit(1)
    eigenstate.x(0)
    qc = qpe_circuit(unitary, eigenstate, n_count)
    simulate_qpe(qc)

def run_qubo():
    print("\n--- Solving QUBO Optimization Problem ---")
    simple_qubo_problem()

def main():
    run_shor()
    run_qft()
    run_qpe()
    run_qubo()

if __name__ == "__main__":
    main()

