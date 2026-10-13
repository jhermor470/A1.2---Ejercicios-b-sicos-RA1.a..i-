"""Ejercicio 1.2.21 - Escribir un programa que pida al usuario que introduzca
una frase en la consola y muestre por pantalla la frase invertida."""


def main():
    frase = input("Introduzca una frase: ")
    print(frase[::-1]) ### [inicio:fin:paso] al poner -1 lee al reves


if __name__ == "__main__":
    main()