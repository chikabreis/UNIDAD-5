# Calcula el área de un círculo dado su radio.
# También verifica si el usuario desea calcular otra área, mostrando un mensaje adecuado.

import math


def calcular_area_circulo(radio):
    """
    Esta función calcula el área de un círculo.

    Parámetros:
    radio (float): El radio del círculo.

    Retorna:
    float: El área del círculo.
    """
    # El área de un círculo se calcula con la fórmula: π * radio^2
    area = math.pi * radio ** 2
    return area


def main():
    # Solicitar al usuario que ingrese el radio del círculo
    radio = float(input("Ingrese el radio del círculo: "))

    # Verificar si el radio es positivo (boolean)
    if radio > 0:
        # Calcular el área utilizando la función definida
        area = calcular_area_circulo(radio)

        # Mostrar el resultado
        print(f"El área del círculo con radio {radio} es {area:.2f}")
    else:
        print("El radio debe ser un número positivo.")
        return  # Salir si el radio no es válido

    # Preguntar al usuario si desea calcular otra área (string)
    respuesta = input("¿Desea calcular el área de otro círculo? (sí/no): ").strip().lower()

    if respuesta == 'sí':
        main()  # Llamar a la función principal de nuevo si la respuesta es sí



# Ejecutar la función principal
if _name_ == "_main_":
    main()