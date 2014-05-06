from conection.conexion import Conexion

class Usuario():

	def __init__(self, idUsuario="", run="", nombre="", apellido="", direccion="", telefono="", email="", fechaNacimiento="", username="", password="", idCategoria=""):
		self.idUsuario = idUsuario
		self.run = run
		self.nombre = nombre
		self.apellido = apellido
		self.direccion = direccion
		self.telefono = telefono
		self.email = email
		self.fechaNacimiento = fechaNacimiento
		self.username = username
		self.password = password
		self.idCategoria = idCategoria

	def findAll(self):
		con = Conexion()
		con.controller = 'usuario.php'
		con.accion = 'findAll'
		resp = con.execute()
		user = []
		for x in resp:
			user.append(Usuario(x["ID_USUARIO"],x["RUN"],x["NOMBRE"],x["APELLIDO"],x["DIRECCION"],x["TELEFONO"],x["EMAIL"],x["FECHA_NACIMIENTO"],x["USERNAME"],x["PASSWORD"],x["ID_CATEGORIA"]))
		return user

	def findByIdUsuario(self, id):
		con = Conexion()
		con.controller = 'usuario.php'
		con.accion = 'findByIdUsuario'
		con.id = id
		resp = con.execute()
		user = []
		if resp is None:
			return None
		else:
			for x in resp:
				user.append(Usuario(x["ID_USUARIO"],x["RUN"],x["NOMBRE"],x["APELLIDO"],x["DIRECCION"],x["TELEFONO"],x["EMAIL"],x["FECHA_NACIMIENTO"],x["USERNAME"],x["PASSWORD"],x["ID_CATEGORIA"]))
			return user

	def findByRun(self, run):
		con = Conexion()
		con.controller = 'usuario.php'
		con.accion = 'findByRun'
		con.id = run
		resp = con.execute()
		user = []
		if resp is None:
			return None
		else:
			for x in resp:
				user.append(Usuario(x["ID_USUARIO"],x["RUN"],x["NOMBRE"],x["APELLIDO"],x["DIRECCION"],x["TELEFONO"],x["EMAIL"],x["FECHA_NACIMIENTO"],x["USERNAME"],x["PASSWORD"],x["ID_CATEGORIA"]))
			return user