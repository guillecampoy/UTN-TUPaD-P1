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
print_separator("Actividad 1 - ¿Es mayor de edad?")
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

#Ejercicio 7 ¿Termina en vocal?
print_separator("Actividad 7 - ¿Termina en vocal?")

# Variables auxiliares
listadoVocales = ['a', 'e', 'i', 'o', 'u']

palabra = input("Ingrese una palabra: ")
if palabra[-1].lower() in listadoVocales:
    print(Fore.GREEN + palabra +"!")
else:
    print(Fore.RED + palabra)

# Ejercicio 8 Tratamiento de cadenas continuación
print_separator("Actividad 8 - ¿Cómo prefiere su nombre?")
nombre = input("Ingrese su nombre: ")
print("1- Si quiere su nombre en mayúsculas. Por ejemplo JUAN")
print("2- Si quiere su nombre en minúsculas. Por ejemplo juan")
print("3- Si quiere su nombre con primera letra mayúsculas. Por ejemplo Juan")
opcion = int(input("Ingrese una opción: "))
if opcion == 1:
    print(Fore.GREEN + nombre.upper())
elif opcion == 2:
    print(Fore.GREEN + nombre.lower())
elif opcion == 3:
    print(Fore.GREEN + nombre.title())
else:
    print(Fore.RED + "Opción incorrecta")

# Ejercicio 9 Magnitud de terremoto
print_separator("Actividad 9 - Magnitud de terremoto")
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3.0:
    print(Fore.GREEN + "Muy leve (imperceptible)")
elif magnitud >= 3.0 and magnitud < 4.0:
    print(Fore.GREEN + "Leve (ligeramente perceptible)" )
elif magnitud >= 4.0 and magnitud < 5.0:
    print(Fore.YELLOW + "Moderado (sentido por las personas, pero generalmente no causa daños)")
elif magnitud >= 5.0 and magnitud < 6.0:
    print(Fore.YELLOW + "Fuerte (puede causar daños estructuras débiles)")
elif magnitud >= 6.0 and magnitud < 7.0:
    print(Fore.RED + "Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 7.0:
    print(Fore.RED + "Extremo (puede causar graves daños a gran escala)")
else:
    print(Fore.RED + "Error ingreso de magnitud")

# Ejercicio 10 Estacion del año
print_separator("Actividad 10 - Estación del año")
hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))
if hemisferio == 'N':
    if (mes == 3 and dia >= 21) or (mes > 3 and mes < 6) or (mes == 6 and dia <= 20):
        print(Fore.GREEN + "Primavera")
    elif (mes == 6 and dia >= 21) or (mes > 6 and mes < 9) or (mes == 9 and dia <= 20):
        print(Fore.GREEN + "Verano")
    elif (mes == 9 and dia >= 21) or (mes > 9 and mes < 12) or (mes == 12 and dia <= 20):
        print(Fore.GREEN + "Otoño")
    elif (mes == 12 and dia >= 21) or (mes < 3) or (mes == 3 and dia <= 20):
        print(Fore.GREEN + "Invierno")
    else:
        print(Fore.RED + "Error ingreso de fecha")
elif hemisferio == 'S':
    if (mes == 3 and dia >= 21) or (mes > 3 and mes < 6) or (mes == 6 and dia <= 20):
        print(Fore.GREEN + "Otoño")
    elif (mes == 6 and dia >= 21) or (mes > 6 and mes < 9) or (mes == 9 and dia <= 20):
        print(Fore.GREEN + "Invierno")
    elif (mes == 9 and dia >= 21) or (mes > 9 and mes < 12) or (mes == 12 and dia <= 20):
        print(Fore.GREEN + "Primavera")
    elif (mes == 12 and dia >= 21) or (mes < 3) or (mes == 3 and dia <= 20):
        print(Fore.GREEN + "Verano")
    else:
        print(Fore.RED + "Error ingreso de fecha")
else:
    print(Fore.RED + "Error ingreso de Hemisferio")

print_footer()