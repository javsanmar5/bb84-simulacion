from persons.Receiver import Receiver
from persons.Sender import Sender
from persons.Hacker import Hacker
from qubits.Qubit import Qubit
from utils.log import write_log

def bb84_with_hacker(num_qubits: int, hacker: str) -> None:
    a = Sender("A")
    b = Receiver("B")
    c = Hacker(hacker)

    a.generate_qubits(num_qubits)
    c.intercept_and_measure(a.qubits)
    b.measure_qubits(c.qubits)

    print(f"{a.name} ha generado:{ a.qubits }")
    print(f"{b.name} ha medido en las siguientes bases:")
    for qubit in b.qubits:
        print(qubit.basis, end=" | ")

    matching_indices = Qubit.compare_basis(a.qubits, b.qubits)
    
    a.update_qubits(matching_indices)
    b.update_qubits(matching_indices)
    
    print("Los resultados de la comparación son los siguientes:")
    print(f"A: {a.qubits}")    
    print(f"B: {b.qubits}")   

    keys_validated = _validate_keys(a.qubits, b.qubits)

    if keys_validated:
        print("Los qubits coinciden. La clave es segura")
    else:
        print("Los qubits no coinciden. La clave no es segura.")
        
    write_log(keys_validated)

def bb84_with_no_hacker(num_qubits: int) -> None:
    a = Sender("A")
    b = Receiver("B")

    a.generate_qubits(num_qubits)
    b.measure_qubits(a.qubits)

    print(f"{a.name} ha generado:{ a.qubits }")
    input()
    print(f"{b.name} ha medido en las siguientes bases:")
    for qubit in b.qubits:
        print(qubit.basis, end=" | ")

    input()

    matching_indices = Qubit.compare_basis(a.qubits, b.qubits)
    
    a.update_qubits(matching_indices)
    b.update_qubits(matching_indices)
    
    print("Los resultados de la comparacion son los siguientes:")
    print(f"A: {a.qubits}")    
    print(f"B: {b.qubits}")   
    input()

    if _validate_keys(a.qubits, b.qubits):
        print("Los qubits coinciden. La clave es segura")
    else:
        print("Los qubits no coinciden. La clave no es segura.")
  
def _validate_keys(qubits1: list, qubits2: list) -> bool:
    return qubits1 == qubits2
