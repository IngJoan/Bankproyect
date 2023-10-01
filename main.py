#estructura de base de datos K=name : [passw, money]
Database = {"NequiGod":["Root", 1_000_000]}
def accountCreate(name,passw):
    if name not in Database:
        while True:
            contra = int(input("Confirme contraseña"))
            if contra == passw:
                print("your welcome")
                money = int(input("Cuanto dinero vas a ingrsar?"))
                Database[name] = [passw, money]
                break

#Funcion que Autentifica la contraseña del usuario y que deja un maximo de 3 errores si la contraseña existe retorna True de lo contrario retorna False
#si no esta el usuario en la base de datos retorna None

def accountAutentication(name, passw):
    if (name in Database) and (passw == Database[name][0]):
        print("Correct")
        return True
    elif name not in Database:
        print("Ese Usuario no existe")
        return None

    elif (name in Database) and (passw != Database[name][0]):
        print("Wrong password")
        i = 0
        while True:
            Intento = int(input("Intenta otra vez tu clave : "))
            if Intento == Database[name][0]:
                print("Correct")
                return True
            else:
                i += 1
                if i == 3:
                    print(f"Wrong answer you have {3 - i} attemps")
                    return False
                print(f"Wrong answer you have {3 - i} attemps")

#Retornamos el balance de la cuenta del usuario
def bankBalance(name):
    return Database[name][1]

#pasamos dinero de una cuenta a otra.
def Transferencia(name, destino, cantidad):
    if Database[name][1] >= cantidad:
        Database[destino][1] += cantidad
        Database[name][1] -= cantidad
        print("Transaccion Aprobada ", end="\n")
        print(f"Su nuevo balance es {bankBalance(name)}")

    else:
        print("No tienes suficiente dinero")



name = None
passw = None

while True:
    print(""" 
                                    Bienvenido a banco azteca 
    
                                        ¿Que desea hacer?
    1)Crear cuenta                      3)Transferir dinero
    
    2)Entrar a cuenta ya existente      4)Ver balance

    """)
    try:
        UE = int(input("Escriba una opcion"))
    except:
        print("Solo numeros")

    if UE == 1:
        while True:
            name = input("Cual es su nombre : ")
            try:
                passw = int(input("Escriba una contraseña"))
                break
            except:
                print("Solo numeros")
        accountCreate(name, passw)
        name = None
        passw = None


    elif UE == 2:
        while True:
            name = input("Cual es su nombre : ")
            try:
                passw = int(input("Escriba una contraseña"))
                break
            except:
                print("Solo numeros")
        A = accountAutentication(name, passw)
        if A != False:
            print("Correcto")
        else:
            name = None
            Passw = None

    elif (UE == 3) and (name != None):
        while True:
            print("A quien deseas transferir dinero : ")
            dest = input("Escribe la cuenta de destino \n si no deseas transferir dinero escribe 0xx")
            if dest == "0xx" :
                break
            else:
                Transferencia(name, dest, int(input("Cuanto deseas mandar")))
                break


    elif (UE == 3) and (name == None):
        print("Inicie session")

    elif (UE == 4) and (name != None):
        print(bankBalance(name))


    elif (UE == 4) and (name == None):
        print("Inicie session")

    else:
        print("Esa no es una opcion")
