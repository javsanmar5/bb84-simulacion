import random

class Qubit:
    def __init__(self, bit: int, basis: str) -> None:
        self.bit = bit
        self.basis = basis  # 'R' for rectilinear, 'D' for diagonal
        
    def measure(self, measurement_basis: str) -> int:
        if self.basis == measurement_basis:
            return self.bit
        else:
            return random.choice([0, 1])
        
    @staticmethod
    def compare_basis(qubits1, qubits2) -> bool:
        matching_indices = []
        for i, qubit in enumerate(qubits1):
            if qubit.basis == qubits2[i].basis:
                matching_indices.append(i)
        return matching_indices
    
    def __eq__(self, other):
        if isinstance(other, Qubit):
            return self.bit == other.bit and self.basis == other.basis
        return False
    
    def __repr__(self):
        return f"Qubit({self.bit}, {self.basis})"
        

