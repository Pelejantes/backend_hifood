from random import randint
from rest_framework.serializers import ValidationError


def gerar_code(qtdDigitos: int):
    numMax = int(qtdDigitos * '9')
    code = str(randint(0, numMax))
    if len(code) != qtdDigitos:
        casas_decimais_ausentes = qtdDigitos - len(code)
        code = casas_decimais_ausentes * "0" + code
    return code


def serializersValidos(serializers: list):
    validos = True
    for serializer in serializers:
        if not serializer.is_valid():
            validos = False
    return validos


def listarErros(serializers: list):
    error_messages = []
    for serializer in serializers:
        if not serializer.is_valid():
            errors = serializer.errors
            for field, field_errors in errors.items():
                for error in field_errors:
                    if isinstance(error, ValidationError):
                        error_messages.append(f"{field}: {error.message}")
                    else:
                        error_messages.append(f"{field}: {error}")
    return error_messages
