from abc import ABC

class Person(ABC):
    def __init__(self, name: str):
        self.name = name
        self.qubits = []

    def update_qubits(self, matching_indices: list) -> None:
        self.qubits = [self.qubits[i] for i in matching_indices]
        
    def __str__(self):
        return f"{self.name}({self.qubits})"
