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




print_footer()