import json
from conection.conexion import Conexion
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Reserva():
	def __init__(self, idReserva = "", idCancha = "", idUsuario = "", fecha = "", horaInicio = "", estado = ""):
		self.idReserva = idReserva
		self.idCancha = idCancha
		self.idUsuario = idUsuario
		self.fecha = fecha
		self.horaInicio = horaInicio
		self.estado = estado

	def findByIdCanchaAndFecha(self, reserva):
		con = Conexion()
		con.controller = 'reserva.php'
		con.accion = 'findByIdCanchaAndFecha'
		con.json = json.dumps([str(reserva.idCancha), str(reserva.fecha)])
		resp = con.execute()
		reservas = []
		if resp==None:
			return None
		else:
			for x in resp:
				reservas.append(Reserva(x["ID_RESERVA"],x["ID_CANCHA"],x["ID_USUARIO"],x["FECHA"],x["HORA_INICIO"],x["ESTADO"]))
			return reservas

	def add(self, reserva):
		con = Conexion()
		con.controller = 'reserva.php'
		con.accion = 'add'
		con.json = json.dumps([str(reserva.idCancha), str(reserva.idUsuario), str(reserva.fecha),str(reserva.horaInicio),str(reserva.estado)])
		resp = con.executeCUD()
		return resp
	
	def deleteByUserHourAndDate(self, reserva):
		con = Conexion()
		con.controller = 'reserva.php'
		con.accion = 'deleteByUserHourAndDate'
		con.json = json.dumps([str(reserva.idUsuario), str(reserva.fecha), str(reserva.horaInicio)])
		resp = con.executeCUD()
		return resp