"""Ejercicio 1.2.13 - Escribir un programa que pida al usuario dos números
enteros y muestre por pantalla lo siguiente: "la división de n entre m da
un cociente c y un resto r", donde n y m son los números introducidos por el
usuario, y c y r son el cociente y el resto de la división entera
respectivamente. Trata también la división entre cero."""


def main():
    n = int(input("Introduce el primer numero entero: "))
    m = int(input("Introduce el segundo numero entero: "))
    if m == 0:
        print("No se puede dividir entre 0") ### si tiene que dividir entre 0
    else   
        c = n // m
        r = n % m
        print(f"La división de {n} entre {m} da un cociente {c} y un resto {r}")


if __name__ == "__main__":
    main()