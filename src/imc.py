def determinar_condicion_riesgo(peso, estatura, edad):
    imc = peso / (estatura ** 2)
    if edad < 45 and imc < 22.0:
        return "bajo"
    elif edad < 45 or imc >= 22.0:
        return "medio"
    else:
        return "alto"

def evaluar(dia, mes, anno):
    peso = float(input("Ingrese su peso: "))
    estatura = float(input("Ingrese su estatura: "))
    edad = 2024 - anno

    return determinar_condicion_riesgo(peso, estatura, edad)

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(dia, mes, anno)
    print(respuesta)