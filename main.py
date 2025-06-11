import argparse
from src.shor_algorithm import factor_integer
from src.qft_module import create_qft_circuit
from src.qpe_module import simulate_qpe, example_qpe_circuit
from src.qubo_solver import simple_qubo_problem

def main():
    parser = argparse.ArgumentParser(
        description="QUBO Calculator – Run Shor, QFT, QPE, or QUBO from CLI"
    )

    parser.add_argument('--shor', type=int, help='Factor an integer using Shor’s Algorithm')
    parser.add_argument('--qft', type=int, help='Visualize QFT for n qubits')
    parser.add_argument('--qpe', action='store_true', help='Run example Quantum Phase Estimation')
    parser.add_argument('--qubo', action='store_true', help='Solve a sample QUBO problem')
    parser.add_argument('--all', action='store_true', help='Run all algorithms in sequence')

    args = parser.parse_args()

    if args.shor:
        print(f" Factoring {args.shor} with Shor’s Algorithm...")
        print("Result:", factor_integer(args.shor))

    if args.qft:
        print(f" Generating QFT circuit for {args.qft} qubits...")
        create_qft_circuit(args.qft).draw('mpl')

    if args.qpe:
        print(" Running Quantum Phase Estimation...")
        qc = example_qpe_circuit()
        simulate_qpe(qc)

    if args.qubo:
        print(" Solving QUBO problem...")
        solution, cost = simple_qubo_problem()
        print("Solution:", solution)
        print("Cost:", cost)

    if args.all:
        print(" Running complete algorithm showcase...\n")
        print("[1] Shor’s Algorithm (21):", factor_integer(21))
        create_qft_circuit(3).draw('mpl')
        simulate_qpe(example_qpe_circuit())
        sol, cost = simple_qubo_problem()
        print("QUBO → Solution:", sol, "| Cost:", cost)

if __name__ == "__main__":
    main()
