'''
    Work developed by:
        - David Fuentelsaz    
        - Josué Rodríguez
        - Javier Santos
        
    This file is the main file of the project. It simulates the BB84 protocol
    We are gonna use the basis 'R' for rectilinear and 'D' for diagonal
'''
from bb84.bb84_simulations import *
from utils.log import clear_log
from utils.get_args import get_args
from utils.statistics import statistics

def main() -> None:
    
    clear_log()
    num_qubits, hacker, num_iteraciones, verbose = get_args()
    
    for _ in range(num_iteraciones):
        if hacker:
            bb84_with_hacker(num_qubits, verbose)
        else:
            bb84_with_no_hacker(num_qubits)
            
    if hacker:
        statistics()
        
    return


    
if __name__ == "__main__":
   main()
