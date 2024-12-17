import random

from qubits.Qubit import Qubit
from persons.Person import Person

class Sender(Person):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def generate_qubits(self, num_qubits: list) -> None:
        for _ in range(num_qubits):
            self.qubits.append(Qubit(
                bit=random.randint(0, 1), 
                basis=random.choice(["R", "D"]
            )))
            

            
        