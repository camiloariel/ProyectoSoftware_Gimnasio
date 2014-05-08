from conection.conexion import Conexion

class Cancha():
	def __init__(self, idCancha = "", precio = "", descripcion = "", idTipoCancha = ""):
		self.idCancha = idCancha
		self.precio = precio
		self.descripcion = descripcion
		self.idTipoCancha = idTipoCancha

	def findAll(self):
		con = Conexion()
		con.controller = 'cancha.php'
		con.accion = 'findAll'
		resp = con.execute()
		cancha = []
		for x in resp:
			cancha.append(Cancha(x["ID_CANCHA"],x["PRECIO"],x["DESCRIPCION"],x["ID_TIPO_CANCHA"],x["IMG"]))
		return cancha

	def findByIdTipoCancha(self, id):
		con = Conexion()
		con.controller = 'cancha.php'
		con.accion = 'findByIdTipoCancha'
		con.id = id
		resp = con.execute()
		cancha = []
		if resp is None:
			return None
		else:
			for x in resp:
				cancha.append(Cancha(x["ID_CANCHA"],x["PRECIO"],x["DESCRIPCION"],x["ID_TIPO_CANCHA"],x["IMG"]))
			return cancha