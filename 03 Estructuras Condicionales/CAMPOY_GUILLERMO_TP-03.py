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

# Ejercicio 1 solicitud de edad
print_separator("Actividad 1 - ¿Mayor o menor de edad?")
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print(Fore.GREEN + "Es mayor de edad")

# Ejercicio 2 Calificaciones
print_separator("Actividad 2 - Calificaciones")
calificacion = float(input("Ingrese su calificación: "))
if calificacion >= 6:
    print(Fore.GREEN + "Aprobado")
else:
    print(Fore.RED + "Desaprobado")

# Ejercicio 3 Solo pares
print_separator("Actividad 3 - Solo pares")
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print(Fore.GREEN + "Ha ingresado un número par")
else:
    print(Fore.RED + "Por favor, ingrese un número par")

# Ejercicio 4 categorias por edad
print_separator("Actividad 4 - Categorías por edad")
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print(Fore.GREEN + "Niño/a")
elif edad >= 12 and edad < 18:
    print(Fore.GREEN + "Adolescente")
elif edad >= 18 and edad < 30:
    print(Fore.GREEN + "Adulto/a joven")
elif edad >= 30:
    print(Fore.GREEN + "Adulto/a")
else:
    print(Fore.RED + "Error ingreso de edad")

# Ejercicio 5 Longitud de contraseña
print_separator("Actividad 5 - Longitud de contraseña")
contrasena = input("Ingrese su contraseña: ")
if len(contrasena) >= 8 and len(contrasena) <= 14:
    print(Fore.GREEN + "Ha ingresado una contraseña correcta")
else:
    print(Fore.RED + "Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6 Uso lib statistics
print_separator("Actividad 6 - Uso de la librería statistics")
#imports para el ejercicio
from statistics import mode, median, mean
import random

#listado numeros aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

#calculos estadisticos
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

#calculo de sesgos

#positivo media > mediana y mediana > moda
if media > mediana and mediana > moda:
    print(Fore.GREEN + "Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print(Fore.RED + "Sesgo negativo o a la izquierda")
elif media == mediana and mediana == moda:
    print(Fore.GREEN + "Sin sesgo")
else:
    print(Fore.YELLOW + "Indeterminado")      


print_footer()