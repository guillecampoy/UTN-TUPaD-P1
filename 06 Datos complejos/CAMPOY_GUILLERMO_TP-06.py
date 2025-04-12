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

# clases

class Persona:
    # Clase Persona
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar (self):
        return f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años."

class Circulo:
    # Clase Circulo
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

# programa principal
print_header()

# Ejercicio 1 uso de diccionarios
print_separator("Actividad 1 - Uso de diccionarios")

precios_frutas = {
    "Banana": 1200,
    "Ananá": 2500,
    "Melón": 3000,
    "Uva": 1450,
}

print(Fore.YELLOW + Style.BRIGHT + "Frutas y precios (estado inicial):")
for fruta, precio in precios_frutas.items():
    print(Fore.BLUE + Style.BRIGHT + f"{fruta}: ${precio}")

# Se propone añadir nuevas frutas con nuevos precios
precios_frutas.update({
    "Naranja": 1200,
    "Manzana": 1500,
    "Pera": 2300,
})
print()
print(Fore.YELLOW + Style.BRIGHT + "Frutas y precios (estado final):")
for fruta, precio in precios_frutas.items():
    print(Fore.GREEN + Style.BRIGHT + f"{fruta}: ${precio}")

# Ejercicio 2 continuación punto 1 con actualización de precios
print_separator("Actividad 2 - Actualización de precios")

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print()
print(Fore.YELLOW + Style.BRIGHT + "Frutas y precios (actualización ejercicio 2):")
for fruta, precio in precios_frutas.items():
    print(Fore.GREEN + Style.BRIGHT + f"{fruta}: ${precio}")

# Ejercicio 3 creación de lista solo con keys de diccionario
print_separator("Actividad 3 - Lista de claves")
# Se crea una lista con las claves del diccionario
lista_frutas = list(precios_frutas.keys())
print(Fore.YELLOW + Style.BRIGHT + "Lista de frutas:")
for fruta in lista_frutas:
    print(Fore.GREEN + Style.BRIGHT + fruta)

# Ejericio 4 uso de clase persona
print_separator("Actividad 4 - Clase Persona")

persona = Persona("Guillermo", "Argentina", 41)
print(Fore.GREEN + Style.BRIGHT + persona.saludar())

# Ejercicio 5 uso de clase circulo
print_separator("Actividad 5 - Clase Circulo")

# Se define un número arbitrario para el radio
radio = 5
circulo = Circulo(radio)
area = circulo.calcular_area()
perimetro = circulo.calcular_perimetro()

print(Fore.YELLOW + Style.BRIGHT + f"Radio del círculo: {radio}")
print(Fore.GREEN + Style.BRIGHT + f"Área del círculo: {area:.2f}")
print(Fore.GREEN + Style.BRIGHT + f"Perímetro del círculo: {perimetro:.2f}")

print_footer()