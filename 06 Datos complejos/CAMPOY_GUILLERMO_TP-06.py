# funciones auxiliares
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

# clases

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

