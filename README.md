# Implementación de BB84: Criptografía Cuántica

Este repositorio contiene una implementación sencilla del protocolo BB84, uno de los protocolos más conocidos para el intercambio de claves cuánticas. Fue desarrollado como parte de un proyecto para una clase de criptografía.

## Descripción

BB84 es un protocolo de criptografía cuántica que utiliza las propiedades de los estados cuánticos para permitir el intercambio seguro de claves entre dos partes. Este protocolo garantiza que cualquier intento de espionaje sea detectable debido a los principios fundamentales de la mecánica cuántica, como el teorema de no clonación y el colapso del estado cuántico.

La implementación en este repositorio simula el protocolo en un entorno clásico para fines educativos, ilustrando los pasos principales:

1. A y B eligen una base con dos ejes, en este caso rectilínea (R) y diagonal
(D). Para el eje rectilíneo se tienen los estados ⬇ (0) y ⬆ (1). Para el eje
diagonal se tiene ⬉ (0) y ⬈ (1). Como consecuencia, tenemos un sistema
con dos ejes y 4 estados, donde dos de los estados corresponden al bit 0 en
cada uno de los dos ejes y los otros dos al bit 1.
2. A elige aleatoriamente una cadena muy larga de bits clásicos y los escribe
en cubits, eligiendo el eje en el que los proyecta de forma aleatoria también.
3. A le envía a B los qubits mediante un canal cuántico.
4. B elige aleatoriamente en que eje va a medir los qubits que ha recibido.
22
5. B envía a A la lista de sus elecciones de ejes mediante un canal público no
cuántico.
6. A también envía a B la lista de sus elecciones de ejes mediante un canal
público no cuántico.
7. Ambos eliminan aquellas qubits cuyos ejes de medición no coincidan. El
motivo detrás de eso es que si los ejes coinciden, como se vió en el apartado
5.1, la medición tiene que ser la misma. Sin embargo, si el eje de medición es
distinto y el vector está puesto de la forma φ = 0|0〉 + 1|1〉 en el eje original,
es decir, un bit clásico, cuando se mida cada estado tendrá un 50% de
probabilidad de aparecer, por lo que se pierde toda la información del qubit.
8. A le pide a B que publique una sublista de los resultados correctos.
9. Si los resultados son iguales o no se supera un umbral preestablecido de
resultados distintos, se asume que la comunicación es segura y los bits
resultantes de las mediciones no publicadas se usan como clave. En caso
contrario, el algoritmo empieza de nuevo hasta que no se supere el umbral de
errores al finalizar la ejecución.


## Características

- **Simulación clásica**: La implementación utiliza Python para simular las propiedades cuánticas del protocolo.
- **Detección de espionaje**: Incluye un atacante, a elección, que intenta espiar el intercambio de qubits, mostrando cómo el protocolo detecta la interferencia.

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu_usuario/bb84-simulacion.git
   cd bb84-simulacion
    ```

## Ejecución
    
    ```bash
    python src/main.py <num_qubits:int(opcional)> <hacker:str(opcional)>
    ```


Muchas gracias.
