"""Ejercicio 1.2.5 - Escribe un programa que pida el importe sin IVA de
un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla
el precio final del artículo."""


def main():
    importe = float(input("Importe sin IVA: "))
    iva = float(input("Tipo de IVA a aplicar (%): "))
    final = importe * (1 + iva / 100)
    print(f"Precio final:, {final}")

if __name__ == "__main__":
    main()