"""Ejercicio 1.2.2 - Escribe un programa para pedirle al usuario las horas
de trabajo y el precio por hora y calcule el importe total del servicio."""


def main():
    horas = float (input("Horas de trabajo: "))
    precio = float (input("Coste por hora: "))
    print(f"Importe total: {horas * precio}")


if __name__ == "__main__":
    main()