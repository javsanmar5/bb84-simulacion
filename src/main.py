'''
    Work developed by:
        - David Fuentelsaz    
        - Josué Rodríguez
        - Javier Santos
        
    This file is the main file of the project. It simulates the BB84 protocol
    We are gonna use the basis 'R' for rectilinear and 'D' for diagonal
'''
from sys import argv
from bb84.bb84_simulations import *

def main(*args, **kwargs) -> None:
    args = args[0]
    try:
        num_qubits = int(args[0]) if len(args) > 0 else 10
        hacker = args[1] if len(args) > 1 else None
    except ValueError:
        num_qubits= 10
        hacker = args[0] if len(args) > 0 else None
    
    if hacker:
        bb84_with_hacker(num_qubits, hacker)
    else:
        bb84_with_no_hacker(num_qubits)
        
    return


if __name__ == "__main__":
    main(argv[1:])
    
    for _ in range(10000):
        main(argv[1:])
