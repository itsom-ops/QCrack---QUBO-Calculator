import pytest
from src.qubo_solver import simple_qubo_problem


def test_qubo_solution_structure():
    solution, cost = simple_qubo_problem()
    assert isinstance(solution, list)
    assert isinstance(cost, float)
    assert all(bit in [0, 1] for bit in solution)
    assert cost >= 0
