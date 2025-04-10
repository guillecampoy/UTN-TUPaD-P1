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



# Definiciones de funciones auxiliares para los ejercicios propuestos
def imprimir_saludo():
    # Función que imprime "Hola Mundo"
    print(Fore.GREEN + "Hola Mundo!")

def saludar_usuario(nombre):
    # Función que saluda al usuario por su nombre
    print(Fore.GREEN + f"Hola {nombre}!")

def informacion_personal(nombre, apellido, edad, residencia):
    # Función que imprime la información personal del usuario
    print(Fore.GREEN + f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

def calcular_area_circulo(radio):
    # Función que calcula el área de un círculo dado su radio
    import math
    area = math.pi * radio ** 2
    return area
def calcular_perimetro_circulo(radio):
    # Función que calcula el perímetro de un círculo dado su radio
    import math
    perimetro = (2 * math.pi * radio)
    return perimetro

def segundos_a_horas(segundos):
    # Función que convierte segundos a horas
    horas = segundos / 3600
    return horas

## Programa principal
print_header()

# Ejercicio 1 implementación función Hola Mundo
print_separator("Actividad 1 - Hola Mundo")

#Llamada a función auxiliar
imprimir_saludo()

# Ejercicio 2 saludar usuario no nombre por parámetro
print_separator("Actividad 2 - Saludo al usuario")
nombre = input("Ingrese su nombre: ")

#Llamada a función auxiliar
saludar_usuario(nombre)

# Ejercicio 3 información personal con formato
print_separator("Actividad 3 - Información personal")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")

#Llamada a función auxiliar
informacion_personal (nombre, apellido, edad, residencia)

#Ejercicio 4 cálculo de área y perímetro de un circulo
print_separator("Actividad 4 - Cálculo de área y perímetro de un círculo")

radio = float(input("Ingrese el radio del círculo: "))

#Llamada a función auxiliar
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

# Se establecen dos decimales para el área y perímetro
print(Fore.GREEN + f"El área del círculo es: {area:.2f}")
print(Fore.GREEN + f"El perímetro del círculo es: {perimetro:.2f}")

# Ejercicio 5 conversión de segundos a horas
print_separator("Actividad 5 - Conversión de segundos a horas")
segundos = int(input("Ingrese la cantidad de segundos: "))

#Llamada a función auxiliar
horas = segundos_a_horas(segundos)

print(Fore.GREEN + f"{segundos} segundos son {horas} horas.")








print_footer()