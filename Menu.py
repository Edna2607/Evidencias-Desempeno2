from Persona import Persona
from Empleado import Empleado

empleado = Empleado(id=None,
                    nombre=None,
                    apellido=None,
                    correo=None,
                    contraseña=None,
                    cargo=None,
                    salario=None,
                    tipo_contrato=None)


def menuApp():
    print("Inicialice con 1")
    init = int(input("Escriba 1 para ver el menú = "))

    while init != 0:
        print("------------MENU-------------\n"
              "Seleccione 1 - para Registrar empleado\n"
              "Seleccione 2 - para Iniciar sesión\n"
              "Seleccione 3 - para ver los datos del usuario\n"
              "Seleccione 4 - para salir\n"
              "-----------------------------------\n")

        opc = input("Ingrese una opción = ")

        if opc == "1":
            empleado.registrar_usuario()
        elif opc == "2":
            if empleado.iniciar_sesion():
                print("Has iniciado sesión")
        elif opc == "3":
            empleado.imprimir_registro()
        elif opc == '4':
            print("--- Salir ----")
            init = 0


menuApp()
