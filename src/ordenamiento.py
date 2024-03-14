def evaluar(numero1, numero2, numero3, numero4):
    numeros = [numero1, numero2, numero3, numero4]
    numeros.sort()
    return "Números en orden ascendente: " + ' '.join(map(str, numeros))

if __name__ == '__main__':
    print("Número 1:", end="")
    numero1 = int(input())
    print("Número 2:", end="")
    numero2 = int(input())
    print("Número 3:", end="")
    numero3 = int(input())
    print("Número 4:", end="")
    numero4 = int(input())
        
    respuesta = evaluar(numero1, numero2, numero3, numero4)
    print(respuesta)

