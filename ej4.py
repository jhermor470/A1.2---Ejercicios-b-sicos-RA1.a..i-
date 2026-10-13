"""Ejercicio 1.2.4 - Escribe un programa que le pida al usuario una temperatura
en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla
la temperatura convertida."""


def main():
    celcius = float(input("Temperatura en grados Celsius: "))
    fahrenheit = celcius * 9 / 5 + 32
    print(f"La temperatura en grados Fahrenheit es :", fahrenheit)

if __name__ == "__main__":
    main()