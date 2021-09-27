# Validacion de tipo string
# afp = input()
# var = 0
# for i in ["Provida", "Provital"]:
#     if afp == i:
#         var = 1
# if var != 1:
#     while afp != "provida" and afp != "provital" and afp != "afp"  :
#         afp = input()


# Validacion de tipo int
def evaluarNumero(num):
    comas = num.count(".")
    if comas > 1 :
        return False, num
    elif comas == 1:
        nume = num.split(".")
        if nume[0].isdigit() == True and nume[1].isdigit() == True:
            realNumero = float(num)
            return True, realNumero
        else:
            return False , num
    else:
        if num.isdigit() == True:
            return True, int(num)
        else:
            return False, num 
