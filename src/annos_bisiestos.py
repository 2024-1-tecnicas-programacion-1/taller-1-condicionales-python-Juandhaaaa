def evaluar(anno):
    # TODO: Coloca aquí el código del ejercicio 2: Años bisiestos
    if anno % 100 == 0:
        if anno % 400 == 0:
            return "año bisiesto"
        else:
            return "no es un año bisiesto"

if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)
    