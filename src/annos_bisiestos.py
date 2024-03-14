def evaluar(anno):
    if anno % 4 == 0 and (anno % 100 != 0 or anno % 400 == 0):
        return "es bisiesto"
    else:
        return "no es un año bisiesto"

if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)
    