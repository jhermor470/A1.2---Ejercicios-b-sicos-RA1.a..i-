"""Ejercicio 1.2.14 - Una juguetería tiene mucho éxito en dos de sus productos:
payasos y muñecas. Suele hacer venta por correo y la empresa de logística les
cobra por peso de cada paquete así que deben calcular el peso de los payasos y
muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada
muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos
en el último pedido y calcule el peso total del paquete que será enviado."""


def main():
    peso_payaso = 112
    peso_muneca = 75
    payasos = int(input("Número de payasos: "))
    munecas = int(input("Número de munecas: "))
    total = payasos * peso_payaso + munecas * peso_muneca
    print(f"Total de payasos: {payasos} \nTotal de munecas: {munecas} \nPeso total del paquete: {total} g")

if __name__ == "__main__":
    main()