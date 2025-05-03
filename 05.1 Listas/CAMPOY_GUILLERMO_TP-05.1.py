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

# Ejercicoo 3
# Generar una lista vacía y luego agregar 3 valores aleatorios a la misma
print_separator("Actividad 3 - Lista vacía y agregar valores aleatorios")
lista = []
# Agregar 3 valores aleatorios (strings con sentido)
valores_aleatorios = ['UTN', 'Progra I', 'Python']
for valor in valores_aleatorios:
    lista.append(valor)
# Mostrar la lista generada
print(Fore.GREEN + "Lista generada: ")
print(f"{lista}")

# Ejercicio 4
# Dada la lista inicial ["perro", "gato", "conejo", "pez"], 
# reemplazar el segundo y el último por "loro" y "oso" respectivamente
print_separator("Actividad 4 - Reemplazo de elementos en una lista")
lista_animales = ["perro", "gato", "conejo", "pez"]
print(Fore.CYAN + "Lista inicial: ")
print(f"{lista_animales}")
# Reemplazar el segundo elemento (índice 1) y el último (índice -1)
lista_animales[1] = "loro"
lista_animales[-1] = "oso"
print()
# Mostrar la lista generada
print(Fore.CYAN + "Nueva lista con cambiios: ")
print(Fore.GREEN + f"{lista_animales}")

# Ejercicio 5
# Dado un bloque de código indicar con tus palabras que hace
print_separator("Actividad 5 - ¿Qué hace este código?")
bloque_codigo = "numeros = [8, 15, 3, 22, 7]\n" \
                "numeros.remove(max(numeros)\n" \
                "print(numeros)"
print("Bloque de código: ")
print(Fore.CYAN + bloque_codigo)
print()
print(Fore.GREEN + "Descripción: ")
print(Fore.GREEN + "1. Crea una lista llamada 'numeros' con los valores 8, 15, 3, 22, 7\n"
    "2. Determina el elemento mayor de la lista y lo remueve.\n"
    "4. Imprime la lista resultante.")

# Ejercicio 6
# Definir una lista con los números del 10 al 30(incluído), 
# con saltos de 5 en 5 y mostrar por pantalla los dos primeros elementos 
print_separator("Actividad 6 - Lista con saltos de 5 en 5")
numeros_con_saltos = list(range(10, 31, 5))
print(Fore.CYAN + "Lista de números del 10 al 30 con saltos de 5 en 5: ")
print(f"{numeros_con_saltos}")
print()
print(Fore.GREEN + "Resultados:")
print(f"Primer elemento: {numeros_con_saltos[0]}, segundo elemento: {numeros_con_saltos[1]}")

# Ejercicio 7
# Dada una lista de autos ["sedan", "polo", "suran", "gol"]
# modificar el indice 1 y 2 por otros valores de autos, ejemplo "fiesta" y "focus"
print_separator("Actividad 7 - Modificación de elementos en una lista")
lista_autos = ["sedan", "polo", "suran", "gol"]
print(Fore.CYAN + "Lista inicial: ")
print(f"{lista_autos}")
# Modificar el índice 1 y 2
lista_autos[1] = "fiesta"
lista_autos[2] = "focus"
print()
# Mostrar la lista generada
print(Fore.CYAN + "Lista modificada: ")
print(Fore.GREEN + f"{lista_autos}")

# Ejercicio 8
# Crear una lista vacía llamada "dobles" y agregar el doble de 5,10 y 15 usando append()
# Mostrar la lista generada
print_separator("Actividad 8 - Lista de dobles")
dobles = []
# Agregar el doble de 5, 10 y 15
for num in [5, 10, 15]:
    dobles.append(num * 2)
# Mostrar la lista generada
print(Fore.CYAN + "Lista de dobles: ")
print(Fore.GREEN + f"{dobles}")

# Ejercicio 9
# Ejercicio con listas anidadas, representando una lista con las compras de diferentes clientes
print_separator("Actividad 9 - Compras de diferentes clientes")
compras = [
    ["pan", "leche"],
    ["arroz", "fideos", "salsa"],
    ["agua"]
]
# Imprimir lista de compras original
print(Fore.CYAN + "Lista de compras original: ")
for i, cliente in enumerate(compras):
    print(f"Cliente {i + 1}: {cliente}")

# Ejecutar las siguientes acciones:
# 1. Agregar "jugo" a la lista del tercer cliente
compras[2].append("jugo")
# 2. Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
compras[1][1] = "tallarines"
# 3. Eliminar "pan" de la lista del primero cliente
compras[0].remove("pan")
# 4. Imprimir lista resultante
print()
print(Fore.GREEN + "Lista de compras modificada: ")
for i, cliente in enumerate(compras):
    print(f"Cliente {i + 1}: {cliente}")

# Ejercicio 10
# Listas anidadas: Elaborar una lista anidada "lista_anidada" que contenga los siguientes elementos:
# Posición lista_anidada[0]: 15
# Posición lista_anidada[1]: True
# Posición lista_anidada[2][0]: 25.5
# Posición lista_anidada[2][1]: 57.9
# Posición lista_anidada[2][2]: 30.6
# Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.
print_separator("Actividad 10 - Lista anidada")
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
# Imprimir la lista resultante
print(Fore.CYAN + "Lista anidada: ")
print(Fore.GREEN + f"{lista_anidada}")

print_footer()