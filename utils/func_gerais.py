from random import randint

def gerar_code(qtdDigitos):
    numMax = int(qtdDigitos * '9')
    code = str(randint(0,numMax))
    if len(code) != qtdDigitos:
        casas_decimais_ausentes =qtdDigitos - len(code)
        code = casas_decimais_ausentes * "0" + code
    return code