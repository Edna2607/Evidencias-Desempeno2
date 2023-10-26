class Persona:

    def __init__(self, id, nombre, apellido, correo, password):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._password = password

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    def registrar_usuario(self):
        self.id = input(f"Ingrese el id del usuario: ")
        self.nombre = input(f"Ingrese el nombre del usuario: ")
        self.apellido = input(f"Ingrese el apellido del usuario: ")
        self.correo = input(f"Ingrese el correo del usuario: ")
        self.password = input(f"Ingrese la contraseña del usuario: ")

    def imprimir_registro(self):
        print(f"id: {self._id} \n Nombre: {self._nombre} \n Apellido: {self._apellido} \n Correo: {self._correo} \n Contraseña: {self._password}")
