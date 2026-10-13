"""Ejercicio 1.2.7 - Escribe un programa que solicite tres números
al usuario y calcule e imprima por pantalla su suma."""


def main():
    num1 = float(input("Introduce el primer numero: "))
    num2 = float(input("Introduce el segundo numero: "))
    num3 = float(input("Introduce el tercer numero: "))
    print(f"La suma es: {num1 + num2 + num3:.2f}")  


if __name__ == "__main__":
    main()