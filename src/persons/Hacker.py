import random

from persons.Person import Person
from qubits.Qubit import Qubit

class Hacker(Person):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        
        
    def intercept_and_measure(self, qubits: list) -> None:
        for qubit in qubits:
            basis = random.choice(["R", "D"])
            bit_measured = qubit.measure(basis)
            self.qubits.append(Qubit(bit_measured, basis))
            