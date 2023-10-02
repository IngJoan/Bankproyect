import Pysql

name = None
passw = None
A_tentication = None

while True:
    print(""" 
                                    Bienvenido a banco azteca 
    
                                        ¿Que desea hacer?
    1)Crear cuenta                      3)Transferir dinero
    
    2)Entrar a cuenta ya existente      4)Ver balance

    """)
    try:
        UE = int(input("Escriba una opcion:  "))
    except:
        print("Solo numeros")
    if A_tentication ==False:
        break

    if UE == 1:
        while True:
            name = input("Cual es su nombre : ")
            try:
                passw = int(input("Escriba una contraseña"))
                break
            except:
                print("Solo numeros")
        Pysql.accountCreate(name=f"{name}", passw=passw)
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
        A_tentication = Pysql.accountAut(name=name,passw=passw)
        if A_tentication == False:
            print("Cuenta bloqueada")
            break
        elif A_tentication ==None:
            name = None
            Passw = None
        else:
            print(f"Bienvenido {name}")

    elif (UE == 3) and (name != None):
        while True:
            print("A quien deseas transferir dinero : ")
            dest = input("Escribe la cuenta de destino \n si no deseas transferir dinero escribe 0xx")
            if dest == "0xx" :
                break
            else:
                try:
                    Pysql.accountTransfer(name=name, destino=dest, cantidad=abs(int(input("Cuanto dinero deseas transferir :"))))
                    break
                except:
                    print("Solo puedes trasnferir una cantidad de dinero valida")



    elif (UE == 3) and (name == None):
        print("Inicie session")

    elif (UE == 4) and (name != None):
        balance = Pysql.accountBalance(name=name)
        if balance != None:
            print(balance)
            balance = None
        else:
            print("Algo fallo")


    elif (UE == 4) and (name == None):
        print("Inicie session")

    else:
        print("Esa no es una opcion")
