import random

from qubits.Qubit import Qubit
from persons.Person import Person

class Receiver(Person):
    def __init__(self, name: str) -> None:
        super().__init__(name)


    def measure_qubits(self, qubits: list) -> None:
        for qubit in qubits:
            basis = random.choice(["R", "D"])
            bit_measured = qubit.measure(basis)
            self.qubits.append(Qubit(bit_measured, basis))
    