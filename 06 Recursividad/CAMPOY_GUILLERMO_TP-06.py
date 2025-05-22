# funciones auxiliares
# Se utiliza un formato especial para dar color a la salida
# Se importa la librería colorama para dar color a la salida

# imports
from colorama import init, Fore, Style
import math

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

def print_separator(title="Ejercicio XXX"):
    # Espacio en blanco
    print()
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

# Funciones auxiliares
# Funciones básicas para validar entradas de usuario
def validar_entero_positivo(valor):
    """
    Solicita y valida que el valor recibido sea un número entero positivo.
    Si el valor no es válido, vuelve a solicitarlo hasta que lo sea.
    """
    while True:
        try:
            numero = int(valor)
            if numero < 0:
                raise ValueError("El número debe ser positivo.")
            return numero
        except (ValueError, TypeError):
            print("Debe ingresar un número entero positivo.")
            valor = input("Ingrese un número entero positivo: ").strip()

## TP Entrega Recursividad ##

## Programa principal
print_header()

# Ejercicio 1
'''Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
función para calcular y mostrar en pantalla el factorial de todos los números enteros 
entre 1 y el número que indique el usuario'''

print_separator("Actividad 1 - Factorial Recursivo")

def factorial_recursivo(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial_recursivo(numero - 1)

# Solicitar al usuario un número entero positivo
calculo_factorial = input("Ingrese un número entero positivo para calcular su factorial: ")
entero_valido = validar_entero_positivo(calculo_factorial)

for i in range(1, entero_valido + 1):
    print(Fore.GREEN + f"El factorial de {i} es {factorial_recursivo(i)}")

# Ejercicio 2
'''Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
especifique.'''

print_separator("Actividad 2 - Serie de Fibonacci Recursiva")
def fibonacci_recursivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Solicitar al usuario un número entero positivo
calculo_fibonacci = input("Ingrese un número entero positivo para calcular la serie de Fibonacci: ")
entero_valido_fibonacci = validar_entero_positivo(calculo_fibonacci)
print(Fore.YELLOW + f"Serie de Fibonacci hasta la posición {entero_valido_fibonacci}:")
for i in range(entero_valido_fibonacci + 1):
    print(Fore.GREEN + f"Fibonacci({i}) = {fibonacci_recursivo(i)}")

# Ejercicio 3
'''Crea una función recursiva que calcule la potencia de un número base elevado a un 
exponente, utilizando la fórmula 𝑛𝑚 = 𝑛∗𝑛(𝑚−1). Prueba esta función en un 
algoritmo general. '''

print_separator("Actividad 3 - Potencia Recursiva")
def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)

# Solicitar al usuario la base y el exponente
base = input("Ingrese la base (número entero positivo): ")
exponente = input("Ingrese el exponente (número entero positivo): ")
base_valida = validar_entero_positivo(base)
exponente_valido = validar_entero_positivo(exponente)

resultado = potencia_recursiva(base_valida, exponente_valido)
print(Fore.GREEN + f"{base_valida} elevado a {exponente_valido} es {resultado}")

# Ejercicio 4
'''Crear una función recursiva en Python que reciba un número entero positivo en base 
decimal y devuelva su representación en binario como una cadena de texto.'''

print_separator("Actividad 4 - Decimal a Binario Recursivo")
def decimal_a_binario_recursivo(numero):
    if numero == 0:
        return ""
    else:
        return decimal_a_binario_recursivo(numero // 2) + str(numero % 2)
# Solicitar al usuario un número entero positivo
calculo_binario = input("Ingrese un número entero positivo para convertir a binario: ")
entero_valido_binario = validar_entero_positivo(calculo_binario)
resultado_binario = decimal_a_binario_recursivo(entero_valido_binario)

# Si el resultado es una cadena vacía, significa que el número es 0
if resultado_binario == "":
    resultado_binario = "0"

print(Fore.GREEN + f"El número {entero_valido_binario} en binario es: {resultado_binario}")

# Ejercicio 5
'''Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
lo es.'''
print_separator("Actividad 5 - Palíndromo Recursivo")
def es_palindromo_recursivo(palabra):
    # Convertir la palabra a minúsculas y eliminar espacios
    palabra = palabra.lower().replace(" ", "")
    # Caso base: si la longitud de la palabra es 0 o 1, es un palíndromo
    if len(palabra) <= 1:
        return True
    # Comparar el primer y último carácter
    if palabra[0] != palabra[-1]:
        return False
    # Llamada recursiva eliminando el primer y último carácter
    return es_palindromo_recursivo(palabra[1:-1])

# Solicitar al usuario una palabra
calculo_palindromo = input("Ingrese una palabra o frase para verificar si es un palíndromo: ")

# Verificar si es un palíndromo
if es_palindromo_recursivo(calculo_palindromo):
    print(Fore.GREEN + f"La palabra '{calculo_palindromo}' es un palíndromo.")
else:
    print(Fore.RED + f"La palabra '{calculo_palindromo}' no es un palíndromo.")



print_footer()