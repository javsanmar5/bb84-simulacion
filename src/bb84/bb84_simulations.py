from persons.Receiver import Receiver
from persons.Sender import Sender
from persons.Hacker import Hacker
from qubits.Qubit import Qubit
from utils.log import write_log

def bb84_with_hacker(key_size: int, verbose: bool) -> None:
    a = Sender("A")
    b = Receiver("B")
    c = Hacker("C")

    if key_size < 1:
        num_qubits = 10 * key_size
    else:
        num_qubits = 4 * key_size

    a.generate_qubits(num_qubits)
    c.intercept_and_measure(a.qubits)
    b.measure_qubits(c.qubits)

    if verbose:
        print("\n\n-----------------------------------------------------\n\n")    

        print(f"{a.name} ha generado:{ a.qubits }")
        print(f"{c.name} se ha metido en medio y ha medido en las siguientes bases:")
        for qubit in c.qubits:
            print(f"| {qubit.basis} |", end="")
        print(f"\n{b.name} ha medido en las siguientes bases:")
        for qubit in b.qubits:
            print(f"| {qubit.basis} |", end="")

    matching_indices = Qubit.compare_basis(a.qubits, b.qubits)
    a.update_qubits(matching_indices)
    b.update_qubits(matching_indices)
    
    if verbose:
        print("\nLos resultados de la comparación son los siguientes:")
        print(f"A: {a.qubits}")    
        print(f"B: {b.qubits}")   

    keys_validated = _validate_keys(a, b, key_size)

    if verbose:
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
    print(f"A: {a}")    
    print(f"B: {b}")   
    input()

    if _validate_keys(a.qubits, b.qubits, num_qubits):
        print("Los qubits coinciden. La clave es segura")
    else:
        print("Los qubits no coinciden. La clave no es segura.")
  
def _validate_keys(a, b, key_size) -> bool:
    for i in range(len(a.qubits)):
        if i == key_size:
            break
        if a.qubits[i].bit != b.qubits[i].bit:
            return True
    return False
