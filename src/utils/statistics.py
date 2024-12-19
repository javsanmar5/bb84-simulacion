from collections import Counter

def statistics(trues: int, iterations: int) -> None:
    if input("¿Quieres ver las estadísticas de la simulación? [s/N]").lower() != "s":
        return 
        
    return print(f"Estadísticas de la simulación:\n\n{trues/iterations}")
