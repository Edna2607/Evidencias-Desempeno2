"""Generar un programa que permita hacer el registro e iniciar sesion todo dentro de un while debe imprimir 
el menu usando la implementacion de= if / ifelse (selector multiple) 
cuando inicie sesion que implemente la solucion del calculo de cuotas creada en el reto anterior


print("Bienvenido")
print("1.Registro\n 2.Login\n 3.Salir\n")

print(input("Seleccione una de las opciones = "))

# EL MENU

def menu():
    datos_registro = None
    opcion = "1"
    while True:
        if opcion == "1":
            datos_registro = registro()
            opcion = "2"
        elif opcion == "2":
            if datos_registro is not None:
                if login(datos_registro):
                    print("Login Correcto")
                    opcion = "3"
                else:
                    print("Login Incorrecto")
                    break
            else:
                print("Primero debe Registrarse")
                break
        elif opcion == "3":
            if datos_registro is not None:
                compras()
                break
            else:
                print("Primero debe Registrarse")
                break

# ------- FORMULARIO DE REGISTRO --------
def registro():
    print("Formulario de Registro")
    usuario = input("Ingrese el usuario : ")
    contraseña = input("ingrese su contraseña : ")
    return usuario, contraseña

# ------- FORMULARIO DEL LOGIN ----------
def login(datos_registro):
    print("Formulario de Login")
    usuario = input("Ingrese el usuario : ")
    contraseña = input("ingrese su contraseña : ")
    if usuario == datos_registro[0] and contraseña == datos_registro[1]:
        return True
    else:
        return False

# -------- FORMULARIO DE LAS COMPRAS ---------  
def compras():
    valor_compra = float(input("Valor de la Compra : "))
    num_cuotas = int(input("Numero de cuotas a pagar : "))
    valor_cuota = valor_compra / num_cuotas
    print(f"El valor de cada cuota es : {valor_cuota}")
    while valor_compra > 0:
          pago = float(input("Ingrese el pago : "))
          if pago == valor_cuota:
             valor_compra -= pago
             num_cuotas -= 1
             print(f"Quedan {num_cuotas} cuotas por pagar")
          else:
              print("El pago no es igual al valor de la cuota") """

#-------------------------------------------------------------

# Variables globales para almacenar los datos de registro
datos_registro = None

# ------- FORMULARIO DE REGISTRO --------
def registro():
    print("------- Formulario de Registro ----------- ")
    usuario = input("Ingrese el usuario : ")
    contraseña = input("Ingrese su contraseña : ")
    return usuario, contraseña

# ------- FORMULARIO DEL LOGIN ----------
def login():
    global datos_registro
    print(" ------ Formulario de Login --------- ")
    usuario = input("Ingrese el usuario : ")
    contraseña = input("Ingrese su contraseña : ")
    
    if datos_registro is not None and usuario == datos_registro[0] and contraseña == datos_registro[1]:
        return True
    else:
        return False

# -------- FORMULARIO DE LAS COMPRAS ---------  
def compras():
    valor_compra = float(input("Valor de la Compra : "))
    num_cuotas = int(input("Numero de cuotas a pagar : "))
    valor_cuota = valor_compra / num_cuotas
    print(f"El valor de cada cuota es : {valor_cuota:.2f}")
    
    while valor_compra > 0:
        pago = float(input("Ingrese el pago : "))
        if  pago == valor_cuota:
            valor_compra -= pago
            num_cuotas -= 1
            print(f"Quedan {num_cuotas} cuotas por pagar de = " , valor_cuota)
            print("Restante por pagar: " ,valor_compra)
        else:
            print("El pago no es igual al valor de la cuota")

# Bucle principal
while True:
    print(" ----------- Seleccione una opción: --------------")
    print("1. Registro")
    print("2. Iniciar Sesión")
    print("3. Salir")
    
    opcion = input("Ingrese el número de opción: ")
    
    if opcion == "1":
        datos_registro = registro()
    elif opcion == "2":
        if datos_registro is not None and login():
            print(" ------ Inicio de sesión exitoso. ----------")
            print(" INGRESANDO DATOS DE SU COMPRA =  ")
            compras()
        else:
            print(" ------- Inicio de sesión fallido o no se ha registrado. ----------------- ")
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Seleccione una opción válida.")



                 