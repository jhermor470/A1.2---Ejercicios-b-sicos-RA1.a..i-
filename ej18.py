"""Ejercicio 1.2.18 - Escribir un programa que pregunte el nombre completo del
usuario en la consola y después muestre por pantalla el nombre completo del
usuario tres veces, una con todas las letras minúsculas, otra con todas las letras
mayúsculas y otra solo con la primera letra del nombre y de los apellidos en
mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas
como quiera."""


def main():
    nombre = input("Nombre completo: ")
    print(nombre.lower() + "\t" + nombre.upper() + "\t" + nombre.title())
    
    ###print(nombre.lower()) todas minusculas
    ###print(nombre.upper()) todas mayusculas
    ###print(nombre.title()) las primeras en mayusculas y el resto minusculas


if __name__ == "__main__":
    main()