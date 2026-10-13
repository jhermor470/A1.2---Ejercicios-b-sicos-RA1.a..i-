"""Ejercicio 1.2.9 - ¿Es posible escribir el programa del ejercicio 1.2.7
sin usar variables? Inténtalo."""


def main():
    print(f"La suma es: {float(input('Introduce el primer numero: ')) + float(input('Introduce el segundo numero: ')) + float(input('Introduce el tercer numero: ')):.2f}")
#En la misma linea incluimos todo
if __name__ == "__main__":
    main()