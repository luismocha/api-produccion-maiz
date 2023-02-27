def vcedula(cedula):
    # sin ceros a la izquierda
    if len(cedula) != 10:
        return False
    if not cedula.isdigit():
        return False
    if int(cedula[0:2]) < 1 or int(cedula[0:2]) > 24:
        return False

    digito_verificador = int(cedula[9])
    suma = 0
    for i, digito in enumerate(cedula[0:9]):
        digito = int(digito)
        if i % 2 == 0:
            digito *= 2
            if digito > 9:
                digito -= 9
        suma += digito

    total = 10 - (suma % 10)
    if total == 10:
        total = 0

    return total == digito_verificador