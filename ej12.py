"""Ejercicio 1.2.12 - Escribir un programa que pida al usuario su peso (en kg)
y estatura (en metros), calcule el índice de masa corporal y lo almacene en una
variable, y muestre por pantalla la frase Tu índice de masa corporal es donde
es el índice de masa corporal calculado redondeado con dos decimales."""


def main():
    estatura = float(input("Introduce tu estatura (en metros)" ))
    peso = float(input("Introduce tu peso (en KG)"))
    imc = estatura / peso ** 2
    print(f"Tu índice de masa corporal es: {imc:.2f}")

    
if __name__ == "__main__":
    main()