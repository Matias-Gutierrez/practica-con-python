def valnum(numero):
    comas = numero.count(".")
    if comas > 1:
        return False, numero
    elif comas == 1:
        numero = numero.split(".")
        if numero[0].isdigit() == True and  numero[1].isdigit() == True:
            return True, numero
        else:
            return False, numero
        
    else:
        if numero.isdigit() == True:
            return True,numero
        else:
            return False,numero

