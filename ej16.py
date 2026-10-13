"""Ejercicio 1.2.16 - Una panadería vende barras de pan a 3.49€ cada una. El pan
que no es el día tiene un descuento del 60%. Escribir un programa que comience
leyendo el número de barras vendidas que no son del día. Después el programa debe
mostrar el precio habitual de una barra de pan (establecido en el programa como
una constante), el descuento que se le hace por no ser fresca y el coste final
total de todas las barras no frescas."""


def main():
    precio = 3.49
    descuento = 0.60
    barras = int(input("Número de barras vendidas que no son del día: "))
    precio_rebajado = precio * (1 - descuento)
    total = barras * precio_rebajado
    print(f"Precio habitual de una barra: {precio:.2f} €")
    print(f"Descuento por no ser fresca: {descuento * 100:.0f}%")
    print(f"Coste final total: {total:.2f} €")


if __name__ == "__main__":
    main()