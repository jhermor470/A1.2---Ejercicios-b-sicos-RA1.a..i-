"""Ejercicio 1.2.11 - Escribir un programa que lea un entero positivo, n,
introducido por el usuario y después muestre en pantalla la suma de todos
los enteros desde 1 hasta n. La suma de los n primeros enteros positivos
puede ser calculada de la siguiente forma:"""


def main():
    n = int (input("Introduce el numero entero positivo: "))
    suma = (n * (n + 1) // 2)
    print(f"La suma de todos los enteros de 1 hasta {n} es: {suma}")


if __name__ == "__main__":
    main()