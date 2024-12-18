
def clear_log() -> None:
    with open('logs/log.txt', 'w') as file:  
        file.write("")
        

def write_log(keys_validated: bool) -> None:
    with open('logs/log.txt', 'a') as file:  
        to_write = 'T' if keys_validated else 'F'
        file.write( to_write + '\n')
