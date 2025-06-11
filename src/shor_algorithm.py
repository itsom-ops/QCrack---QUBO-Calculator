from qiskit.algorithms import Shor
from qiskit.utils import QuantumInstance
from qiskit import Aer
import time

def factor_integer(N: int) -> list:
    """
    Executes Shor's Algorithm to factor a given integer N using Qiskit's built-in implementation.

    Parameters:
        N (int): Integer to factorize (should be a composite number > 1)

    Returns:
        list: A list containing non-trivial factors of N, or an empty list if unsuccessful.
    """
    if N < 2:
        raise ValueError("Input integer must be greater than 1.")

    backend = Aer.get_backend('aer_simulator')
    instance = QuantumInstance(backend=backend, shots=2048)

    start_time = time.time()
    shor = Shor(quantum_instance=instance)
    result = shor.factor(N)
    end_time = time.time()
    elapsed_time = end_time - start_time

    print("Shor's Algorithm Execution Report")
    print("----------------------------------")
    print(f"Input Integer        : {N}")
    print(f"Execution Time       : {round(elapsed_time, 4)} seconds")

    if result.factors and result.factors[0]:
        print(f"Non-trivial Factors  : {result.factors[0]}")
        return result.factors[0]
    else:
        print("No non-trivial factors found. Shor's algorithm did not succeed for this input.")
        return []

