import mysql.connector
def bankconnect():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Bank")
        cur = mydb.cursor()
        print("Conexion exitosa")
        return cur, mydb
    except mysql.connector.Error as err:
        print(f"Error : {err}")
        return None, None

cur, mydb = bankconnect()

def accountCreate(name=None, passw=None, cursor=cur):
    if name is not None or passw is not None:
        print("Con cuanto deseas abrir tu cuenta : ", end="\n")
        UI = int(input(""))
        Query = f"INSERT INTO customers (name,passw,balance) VALUES('{name}', {passw}, {UI});"
        try:
            cursor.execute(Query)
            mydb.commit()  # Asegura de confirmar los cambios en la base de datos
            print("Todo ha salido bien")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    else:
        print("Es obligatorio Tener los parametros de nombre y/o contraseña")

#Verificamos la contraseña de la cuenta
#si el usuario no existe se retorna None y se imprime usuario incorrecto
#si la contraseña esta mal se dan 3 intentos mas y si no es correcta retorna False
#sitodo esta bien se retorna name y se imprime bienvenido

def accountAut(name=None, passw=None, cursor=cur):
    if name is not None and passw is not None:
        cursor.execute(f"SELECT passw FROM Customers WHERE name='{name}';")
        dato = cursor.fetchall()
        try:
            if dato[0][0] == passw:
                print(f"Bienvenido {name}")
                return name
            else:
                Intentos = 3
                while True:
                    print("Contraseña incorrecta")
                    print(f"Te quedan {Intentos}")
                    if Intentos >= 0:
                        Intentos -= 1
                        Np = int(input("Vuelve a intentarlo : "))
                        if dato[0][0] == Np:
                            print(f"Bienvenido {name}")
                            return name
                    else:
                        return False
        except IndexError:
            print("Usuario no encontrado")
            return None

def accountBalance(name=None, cur=cur):
    if name != None:
        cur.execute(f"SELECT balance FROM customers WHERE name='{name}';")
        balance = cur.fetchall()[0][0]
        return balance
    else:
        print("Usuario {name} no encontrado")
        return None

def accountTransfer(name=None, destino=None, cantidad=0, cur=cur):
    if (name is not None) and (destino is not None):
        try:
            __Query = f"SELECT * FROM customers WHERE name='{destino}';"
            cur.execute(__Query)
            x = cur.fetchall()
            x[0][0] #Esto solo es para confirmar que exista el destino si no salta error y va al except
            if accountBalance(name) >= cantidad:
                print("En proceso")
                dindes = accountBalance(destino)
                dinu = accountBalance(name)
                cur.execute(f"UPDATE customers SET balance={dinu - cantidad} WHERE name='{name}';")
                mydb.commit()
                print(f"Tu nuevo balance es : {accountBalance(name)}")
                cur.execute(f"UPDATE customers SET balance={dindes + cantidad} WHERE name='{destino}';")
                mydb.commit()
            else:
                print("Dinero no suficiente")
        except:
            print("Destino no Encontrado")
            return None