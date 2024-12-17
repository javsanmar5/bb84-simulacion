from persons.Receiver import Receiver
from persons.Sender import Sender
from persons.Hacker import Hacker
from qubits.Qubit import Qubit


def bb84_with_hacker(num_qubits: int, hacker: str) -> None:
    a = Sender("A")
    b = Receiver("B")
    c = Hacker(hacker)

    a.generate_qubits(num_qubits)
    c.intercept_and_measure(a.qubits)
    b.measure_qubits(c.qubits)

    print(f"{a.name} has generated: {a.qubits}")
    # input()
    print(f"{b.name} has measured in the following basis:")
    for qubit in b.qubits:
        print(qubit.basis, end=" | ")

    # input()

    matching_indices = Qubit.compare_basis(a.qubits, b.qubits)
    
    a.update_qubits(matching_indices)
    b.update_qubits(matching_indices)
    
    print("They results after the comparison are:")
    print(f"A: {a.qubits}")    
    print(f"B: {b.qubits}")   
    # input()

    if _validate_keys(a.qubits, b.qubits):
        print("The qubits match. The key is secure.")
    else:
        print("The qubits don't match. The key is not secure.")

def bb84_with_no_hacker(num_qubits: int) -> None:
    a = Sender("A")
    b = Receiver("B")

    a.generate_qubits(num_qubits)
    b.measure_qubits(a.qubits)

    print(f"{a.name} has generated:{ a.qubits }")
    input()
    print(f"{b.name} has measured in the following basis:")
    for qubit in b.qubits:
        print(qubit.basis, end=" | ")

    input()

    matching_indices = Qubit.compare_basis(a.qubits, b.qubits)
    
    a.update_qubits(matching_indices)
    b.update_qubits(matching_indices)
    
    print("They results after the comparison are:")
    print(f"A: {a.qubits}")    
    print(f"B: {b.qubits}")   
    input()

    if _validate_keys(a.qubits, b.qubits):
        print("The qubits match. The key is secure.")
    else:
        print("The qubits don't match. The key is not secure.")
  
def _validate_keys(qubits1: list, qubits2: list) -> bool:
    with open('logs/log.txt', 'a') as file:  
        to_write = 'T' if qubits1 == qubits2 else 'F'
        file.write(to_write + '\n')
    return qubits1 == qubits2
