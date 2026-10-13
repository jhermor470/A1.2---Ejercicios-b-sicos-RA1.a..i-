"""Ejercicio 1.2.17 - Escribir un programa que pregunte el nombre del usuario
en la consola y un número entero e imprima por pantalla en líneas distintas el
nombre del usuario tantas veces como el número introducido."""


def main():
    nombre = (input("Cual es tu nombre: "))
    numero = int(input("Introduce un numero entero: "))
    print ((nombre + "\n") * numero) ###se incluye el salto de linea

if __name__ == "__main__":
    main()