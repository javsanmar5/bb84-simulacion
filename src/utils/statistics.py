from collections import Counter

def statistics() -> None:
    if input("¿Quieres ver las estadísticas de la simulación? [s/N]").lower() != "s":
        return 
        
    data = read_log()
    if data:
        ratio = _get_statistics(data)
        print(f"Ratio of 'T': {ratio}")
    else:
        print("No data to analyze.")

def read_log() -> list:
    try:
        with open('logs/log.txt', 'r') as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        print("Log file not found.")
        return []

def _get_statistics(data: list) -> float:
    counts = Counter(data)
    t_count = counts.get("T", 1) 
    
    return t_count / len(data)
