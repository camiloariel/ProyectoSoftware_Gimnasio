from conection.conexion import Conexion

class TipoCancha():

	def __init__(self, idTipoCancha = "", nombre = ""):
		self.idTipoCancha = idTipoCancha
		self.nombre = nombre

	def findAll(self):
		con = Conexion()
		con.controller = 'tipo_cancha.php'
		con.accion = 'findAll'
		resp = con.execute()
		tCancha = []
		for x in resp:
			tCancha.append(TipoCancha(x["ID_TIPO_CANCHA"],x["NOMBRE"]))
		return tCancha