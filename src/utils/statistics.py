from collections import Counter

def statistics(trues: int, iterations: int) -> None:
    if input("\n¿Quieres ver las estadísticas de la simulación? [s/N]").lower() != "s":
        return 
        
    print("\n\n----------Estadísticas de la simulación ----------")
    result = ((iterations-trues) / iterations) * 100
    print(f"El porcentaje de vez que se ha pillado al hacker es {result}%")
    return
