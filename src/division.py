def evaluar(dividendo, divisor):
    cociente = dividendo // divisor
    residuo = dividendo % divisor

    if residuo == 0:
        print("La división es exacta")
    else:
        print("La división no es exacta")

    print("Cociente:", cociente)
    print("Residuo:", residuo)

if __name__ == '__main__':
    dividendo = int(input("Dividendo: "))
    divisor = int(input("Divisor: "))

    evaluar(dividendo, divisor)
