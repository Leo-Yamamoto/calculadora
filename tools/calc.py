def calcular(visor):
    try:
        resultado = eval(visor)
        return str(resultado)
    except:
        return "Erro"
    