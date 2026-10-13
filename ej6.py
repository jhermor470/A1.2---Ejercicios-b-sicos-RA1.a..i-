"""Ejercicio 1.2.6 - Escribe un programa que pida el importe final de un
artículo y calcule e imprima por pantalla el IVA que se ha pagado y el
importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%)."""


def main():
    iva = 1.10
    importe = float(input("Importe del articulo: "))
    #Restamos 1, multiplicamos por 100 y formateamos a 0 decimales con :.0f
    print(f"IVA pagado: {(iva - 1) * 100:.0f} \nImporte sin IVA: {importe / iva:.2f}")


if __name__ == "__main__":
    main()