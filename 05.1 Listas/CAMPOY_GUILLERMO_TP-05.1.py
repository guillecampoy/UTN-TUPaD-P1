# Se utiliza un formato especial para dar color a la salida
# Se importa la librería colorama para dar color a la salida

from colorama import init, Fore, Style
# Inicializa Colorama
init(autoreset=True)

def print_header():
    # Imprime el encabezado del programa
    print(Fore.CYAN + Style.BRIGHT + "=" * 60)
    print(Fore.CYAN + Style.BRIGHT + r"""
    .----------------------.
    |                      |
    |  U   U TTTTTT N   N  |
    |  U   U   TT   NN  N  |
    |  U   U   TT   N N N  |
    |  U   U   TT   N  NN  |
    |   UUU    TT   N   N  |
    |                      |
    '----------------------'
    """)
    print(Fore.CYAN + Style.BRIGHT + "Universidad Tecnológica Nacional")
    print(Fore.CYAN + Style.BRIGHT + "Campoy Guillermo")
    print(Fore.CYAN + Style.BRIGHT + "Comisión 11")
    print(Fore.CYAN + Style.BRIGHT + "Abril 2025")
    print(Fore.CYAN + Style.BRIGHT + "=" * 60)
print()

def print_separator(title="Resultado"):
    # Imprime un separador con el título dado
    print(Fore.YELLOW + "-" * 60)
    print(Fore.YELLOW + f"{title.center(60)}")
    print(Fore.YELLOW + "-" * 60)

def print_footer():
    # Imprime el pie de página del programa
    print()
    print(Fore.GREEN + Style.BRIGHT + "=" * 60)
    print(Fore.GREEN + Style.BRIGHT + "¡Fin de la ejecución!".center(60))
    print(Fore.GREEN + Style.BRIGHT + "=" * 60)
    print()

## Programa principal
print_header()

# Ejercicio 1
# Generar una lista con los números del 1 al 100, múltiplos de 4 utilizando la función range()
print_separator("Actividad 1 - Lista de múltiplos de 4 entre 1 y 100")
numeros = list(range(1, 101))
multiplos_de_4 = [num for num in numeros if num % 4 == 0]

# Presentación de resultados
print(Fore.CYAN + "Lista de números del 1 al 100: ")
print(f"{numeros}")
print(Fore.GREEN + "Números múltiplos de 4: ")
print(f"{multiplos_de_4}")


# Ejercicio 2
# Generar una lista con elementos aleatorios pero con sentido ejemplo,
#  strings y mostrar el antepenúltimo elemento
print_separator("Actividad 2 - Antepenúltimo elemento de una lista aleatoria")
import random
# Generar una lista de 10 elementos aleatorios
elementos_aleatorios = [random.choice(['Hola', 42, 3.14, True, 'Mundo']) for _ in range(10)]
# Mostrar la lista generada
print(Fore.CYAN + "Lista de elementos aleatorios: ")
print(f"{elementos_aleatorios}")
print()
# Mostrar el antepenúltimo elemento, sabiendo que tenemos una lista de 10 elementos
antepenultimo_elemento = elementos_aleatorios[-3]
print(Fore.GREEN + f"Antepenúltimo elemento: ")
print(f"{antepenultimo_elemento}")






print_footer()