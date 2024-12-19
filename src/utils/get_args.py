def get_args() -> tuple:

    num_qubits = None
    num_iteraciones = None
    verbose = False
    
    print("Esto es una implementación simple del protocolo BB84")
    print("Realizada por \n\t- David Fuentelsaz \n\t- Josué Rodríguez\n\t- Javier Santos")
    print("")
    print("-------------------------------------------------------------------")
    print("")
    
    while num_qubits == None:
        try:
            num_qubits = int(input("\nIntroduce el tamaño de la clave: \t\t"))
        except ValueError:
            print("Introduce un entero")
            
    hacker = input("\n¿Quieres añadir un hacker? [s/N]\t\t").lower() == "s"

    if hacker:
        while num_iteraciones == None:
            try:
                num_iteraciones = int(input("\nIntroduce el número de iteraciones: \t\t"))
            except ValueError:
                print("Introduce un entero")
    else:
        num_iteraciones = 1
    
    if hacker:
        verbose = input("\n¿Quieres ver los resultados detallados? \nEsto hará más lento el proceso[s/N]\t\t").lower() == "s"

    return num_qubits, hacker, num_iteraciones, verbose
                
