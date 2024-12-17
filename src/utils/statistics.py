from collections import Counter

def read_log() -> list:
    try:
        with open('logs/log.txt', 'r') as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        print("Log file not found.")
        return []

def statistics(data: list) -> float:
    counts = Counter(data)
    t_count = counts.get("T", 1) 
    
    return t_count / len(data)

if __name__ == '__main__':
    data = read_log()
    if data:
        ratio = statistics(data)
        print(f"Ratio of 'T': {ratio}")
    else:
        print("No data to analyze.")