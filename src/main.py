'''
    Work developed by:
        - David Fuentelsaz    
        - Josué Rodríguez
        - Javier Santos
        
    This file is the main file of the project. It simulates the BB84 protocol
    We are gonna use the basis 'R' for rectilinear and 'D' for diagonal
'''
from bb84.bb84_simulations import *
from utils.get_args import get_args
from utils.statistics import statistics

def main() -> None:
    
    key_size, hacker, iterations, verbose = get_args()
    trues = 0
    print("\n\n\nComenzando simulación de BB84...\n\n\n")
    
    for _ in range(iterations):
        if hacker:
            if bb84_with_hacker(key_size, verbose):
                trues += 1
        else:
            bb84_with_no_hacker(key_size)
            
    if hacker:
        statistics(trues, iterations)
        
    return


    
if __name__ == "__main__":
    main()
    input("\n\n\nPulsa ENTER para salir")