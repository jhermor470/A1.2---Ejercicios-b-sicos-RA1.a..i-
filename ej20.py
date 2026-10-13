"""Ejercicio 1.2.20 - Los teléfonos de una empresa tienen el siguiente formato
prefijo-número-extension donde el prefijo es el código del país +34, y la
extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa
que pregunte por un número de teléfono con este formato y muestre por pantalla
el número de teléfono sin el prefijo y la extensión."""


def main():
    telefono = input("Teléfono (+34-913724710-56): ")
    partes = telefono.split("-") ### recorta el texto cada vez que encuentra un guion
    print(f"Número sin prefijo ni extensión: {partes[1]}") ### si en partes pongo 0 da el +34 y si pongo 2 56


if __name__ == "__main__":
    main()