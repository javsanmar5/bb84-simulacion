from collections import Counter

def statistics() -> None:
    if input("¿Quieres ver las estadísticas de la simulación? [s/N]").lower() != "s":
        return 
        
    data = read_log()
    if data:
        ratio = _get_statistics(data)
        print(f"El porcentaje de veces que se ha capturado al hacker ha sido: {ratio}")
    else:
        print("No hay datos que analizar.")

def read_log() -> list:
    try:
        with open('logs/log.txt', 'r') as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        print("No se encontró el archivo.")
        return []

def _get_statistics(data: list) -> float:
    counts = Counter(data)
    t_count = counts.get("F", 1) 
    
    return t_count / len(data)
