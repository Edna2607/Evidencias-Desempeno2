from Persona import Persona

# Esto importa la clase persona para ser usado en otra clase

# en Empleado hemos importado la clase persona


class Empleado(Persona):

    def __init__(self, id, nombre, apellido, correo, contraseña, cargo, salario, tipo_contrato):
        super().__init__(id, nombre, apellido, correo, contraseña)
        self.cargo = cargo
        self.salario = salario
        self._tipo_contrato = tipo_contrato

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, cargo):
       self._cargo = cargo


    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario


    @property
    def tipo_contrato(self):
        return self._tipo_contrato


    @tipo_contrato.setter
    def tipo_contrato(self, tipo_contrato):
        self._tipo_contrato = tipo_contrato

        # Vamos a sobre escribir los metodos

    def registrar_usuario(self):
      self._id = input(f"Ingrese el id del usuario: ")
      self._nombre = input(f"Ingrese el nombre del usuario: ")
      self._apellido = input(f"Ingrese el apellido del usuario: ")
      self._correo = input(f"Ingrese el correo del usuario: ")
      self._password = input(f"Ingrese la contraseña del usuario: ")
      self._cargo = input(f"Ingrese el cargo del usuario: ")
      self._salario = float(input(f"Ingrese el salario del usuario: "))
      self._tipo_contrato = input(f"Ingrese el tipo_contrato del usuario: ")

    def imprimir_registro(self):
        super().imprimir_registro()
        print(f"Cargo: {self._cargo} --- Salario:{self._salario} ---  Tipo_contrato:{self._tipo_contrato}")

    def iniciar_sesion(self):
        correo_emp = input("Ingrese el correo registrado: ")
        contras_emp = input("Ingrese la contraseña: ")

        if correo_emp == self._correo and contras_emp == self._password:
            return True
        else:
            return False


    def appEmpleado(self, iniciar_sesion, imprimir_registro):
         iniciar_sesion()==True
         print("has iniciado sesion")
         imprimir_registro()
