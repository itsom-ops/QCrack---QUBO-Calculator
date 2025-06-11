import pytest
from qiskit import Aer

@pytest.fixture
def simulator_backend():
    return Aer.get_backend('aer_simulator')
