def evaluar(a, b, c):
    # TODO: Coloca aquí el código del ejercicio 1: Set de tenis
    if a + b <= c or a + c <= b or b + c <= a:
        return "El triángulo es inválido"
    elif a == b == c:
        return "Es un triángulo equilátero"
    elif a == b or b == c or a == c:
        return "Es un triángulo isósceles"
    else:
        return "Es un triángulo escaleno"

if __name__ == '__main__':
    print("a:", end="")
    a = float(input())
    print("b:", end="")
    b = float(input())
    print("c:", end="")
    c = float(input())
        
    respuesta = evaluar(a, b, c)
    print(respuesta)