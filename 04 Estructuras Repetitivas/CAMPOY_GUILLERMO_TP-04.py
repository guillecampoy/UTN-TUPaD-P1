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

print_header()

# Ejercicio 1 imprimir números del 0 al 100, orden creciente mostrando un número por línea
print_separator("Actividad 1 - Números del 0 al 100")
for i in range(0, 101):
    print(Fore.GREEN + str(i))

# Ejercicio 2 solicitar un numero entero y determinar cantidad de dígitos
print_separator("Actividad 2 - Cantidad de dígitos")
numero = int(input("Ingrese un número entero: "))
cantidad_digitos = len(str(abs(numero)))
print(Fore.GREEN + f"La cantidad de dígitos del número {numero} es: {cantidad_digitos}")

# Ejercicio 3 sumar números enteros comprendidos entre dos valores dados por el usuario, excluyendo los valores
print_separator("Actividad 3 - Sumar números enteros")
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))   
suma = 0
# Se verifica cuál es el menor de los dos valores ingresados
# y se utiliza para el rango de la suma
if valor1 < valor2:
    for i in range(valor1 + 1, valor2):
        suma += i
else:
# Se utiliza el valor2 como menor 
# y se invierte el orden de los valores para usar la misma logica de suma    
    for i in range(valor2 + 1, valor1):
        suma += i
print(Fore.GREEN + f"La suma de los números comprendidos entre {valor1} y {valor2} es: {suma}")

#El código anterior incluso se puede resolver con un unico for, validando previamente que
# el valor1 sea menor que el valor2, y si no lo es, se invierten los valores asignados en cada variable
# Puede resultar un poco más confuso, pero es una opción válida.


# Ejercicio 4 ingresar valores hasta obtener 0 (condición de salida) mostrar la suma de los valores ingresados
print_separator("Actividad 4 - Sumar valores hasta ingresar 0")
suma = 0  
# Se realñiza primer lectura fuera del bucle para inicializar la variable
valor = int(input("Ingrese un valor (0 para salir): "))
while valor != 0:
    suma += valor
    valor = int(input("Ingrese un valor (0 para salir): "))
print(Fore.GREEN + f"La suma de los valores ingresados es: {suma}") 

# Ejercicio 5 adivinar número aleatorio entre 0 y 9. Se debe mostrar la cantidad de intentos
print_separator("Actividad 5 - Adivinar número aleatorio")
import random
numero_aleatorio = random.randint(0, 9)
intentos = 0
numero_usuario = int(input("Adivina el número entre 0 y 9: "))
while numero_usuario != numero_aleatorio:
    intentos += 1
    if numero_usuario < numero_aleatorio:
        print(Fore.RED + "El número es mayor.")
    else:
        print(Fore.BLUE + "El número es menor.")
    numero_usuario = int(input("Intenta nuevamente: "))
intentos += 1
print(Fore.GREEN + f"¡Felicidades! Adivinaste el número correcto en {intentos} intentos.")

# Ejercicio 6 listar por pantalla números pares entre 0 y 100 de forma decreciente
print_separator("Actividad 6 - Números pares entre 0 y 100 de forma decreciente")
for i in range(100, -1, -2):
    print(Fore.GREEN + str(i))

# Ejercicio 7 calcular la suma entre 0 y un número dado por el usuario, considerando ingreso de número negativo

print_separator("Actividad 7 - Sumar números hasta un número dado")
numero = int(input("Ingrese un número entero positivo: "))
suma = 0
# Se valida que el número ingresado sea positivo
while numero < 0:
    print(Fore.RED + "El número debe ser positivo.")
    numero = int(input("Ingrese un número entero positivo: "))   

# Con este flujo se incluye la cota superior en la suma 
for i in range(0, numero + 1):
    suma += i
print(Fore.GREEN + f"La suma de los números entre 0 y {numero} es: {suma}")

# Ejercicio 8 se deben ingresar 100 números enteros, luego indicar, cantidad de pares, 
# cantidad impares, cantidad de negativos y cantidad de positivos
print_separator("Actividad 8 - Contar números")
cantidad_numeros = 100
cantidad_pares = 0
cantidad_impares = 0
cantidad_positivos = 0
cantidad_negativos = 0
for i in range(cantidad_numeros):
    numero = int(input("Ingrese un número entero: "))
    if numero % 2 == 0:
        cantidad_pares += 1
    else:
        cantidad_impares += 1
#No se considera el cero como positivo ni negativo
    if numero > 0:
        cantidad_positivos += 1
    elif numero < 0:
        cantidad_negativos += 1
print(Fore.GREEN + f"Cantidad de números pares: {cantidad_pares}")
print(Fore.GREEN + f"Cantidad de números impares: {cantidad_impares}")
print(Fore.GREEN + f"Cantidad de números positivos: {cantidad_positivos}")
print(Fore.GREEN + f"Cantidad de números negativos: {cantidad_negativos}")


print_footer()