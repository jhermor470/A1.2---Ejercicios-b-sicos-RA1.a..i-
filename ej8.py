"""Ejercicio 1.2.8 - Ejercicio 1.2.8 Escribir el programa del ejercicio 1.2.7
usando solamente dos variables diferentes."""


def main():
    num1 = float(input("Introduce el primer numero: "))
    num2 = float(input("Introduce el segundo numero: "))
    num1 += num2 
    num2 = float(input("Introduce el tercer numero: "))
    num1 += num2
    print(f"La suma es: {num1:.2f}")  


if __name__ == "__main__":
    main()