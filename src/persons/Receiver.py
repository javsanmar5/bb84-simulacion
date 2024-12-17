import random

from qubits.Qubit import Qubit
from persons.Person import Person

class Receiver(Person):
    def __init__(self, name: str) -> None:
        super().__init__(name)


    def measure_qubits(self, qubits: list) -> None:
        for qubit in qubits:
            choice = random.choice(["R", "D"])
            if qubit.basis == choice:
                # Se podría añadir directamente el qubit para no crear otro objeto, 
                # pero me da miedo que en algún momento necesite utilizar los qubits 
                # de formas distintas y no quiero que apunten a la misma instancia
                self.qubits.append(Qubit(bit=qubit.bit, basis=qubit.basis)) 
            else:
                self.qubits.append(Qubit(bit=random.randint(0, 1), basis=choice))
                
    