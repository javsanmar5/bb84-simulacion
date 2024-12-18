def get_args() -> tuple:

    num_qubits = None
    num_iteraciones = None
    
    print("Esto es una implementación simple del protocolo BB84")
    print("Realizada por \n\t- David Fuentelsaz \n\t- Josué Rodríguez\n\t- Javier Santos")
    print("")
    print("-------------------------------------------------------------------")
    print("")
    
    while num_qubits == None:
        try:
            num_qubits = int(input("Introduce el número de qubits: "))
        except ValueError:
            print("Introduce un entero")
            
    hacker = input("Introduce el nombre del hacker. Pulsa ENTER si no quieres que haya hacker:\n")

    if hacker:
        while num_iteraciones == None:
            try:
                num_iteraciones = int(input("Introduce el número de iteraciones: "))
            except ValueError:
                print("Introduce un entero")
    else:
        num_iteraciones = 1
                
    return num_qubits, hacker, num_iteraciones
                