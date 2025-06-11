from qiskit_optimization import QuadraticProgram
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit.algorithms import QAOA
from qiskit import Aer
from qiskit.utils import QuantumInstance

def simple_qubo_problem() -> dict:
    """
    Solves a predefined QUBO optimization problem using QAOA as the solver backend.

    The QUBO defined is:
        minimize: x0 + x1 - 2*x0*x1
    which has two binary variables.

    Returns:
        dict: Dictionary with binary variable assignments in the optimal solution.
    """
    problem = QuadraticProgram(name="QUBO_Minimization")
    problem.binary_var(name="x0")
    problem.binary_var(name="x1")
    problem.minimize(linear=[1, 1], quadratic={("x0", "x1"): -2})

    backend = Aer.get_backend("aer_simulator")
    q_instance = QuantumInstance(backend=backend)
    qaoa = QAOA(quantum_instance=q_instance)
    optimizer = MinimumEigenOptimizer(qaoa)

    print("Executing QUBO problem using QAOA...")
    result = optimizer.solve(problem)

    print("QUBO Optimization Result")
    print("------------------------")
    print(f"Optimal Assignment   : {result.variables_dict}")
    print(f"Objective Value      : {result.fval}")
    
    return result.variables_dict

