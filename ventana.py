#! usr/bin/env python
from mainwindow import *
import time
from random import randint, uniform,random
import os
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
		self.showMaximized()
		self.label.setText("")
		self.label_2.setText("")
		self.pushButton.setText("Iniciar")
		self.pushButton.clicked.connect(self.actualizar2)
		self.pushButton_2.clicked.connect(self.reiniciar)
		self.lineEdit.setText("")
		self.lineEdit.textEdited.connect(self.actualizar)
		self.lineEdit.returnPressed.connect(self.evaluar)
		self.spinBox.valueChanged.connect(self.cantidadletras)
		self.deuchland=""
		self.puntaje=0
		self.cletras=1
		self.tiempo=self.cletras
		self.correctas=0
		self.incorrectas=0
		self.nivel=0
		self.level()
		self.lineEdit.setFocus()
		os.system('clear')

		self.temporal()

	def eventFilter(self, source, event):
		if (event.type() == QEvent.KeyPress and source is self.lineEdit):
			print('key press:', (event.key(), event.text()))
			return super(MainWindow, self).eventFilter(source, event)
	

	def level(self):
		self.nivel=int(self.cletras)+int(self.correctas)/(self.incorrectas+10)
		
	def cantidadletras(self):
		self.cletras=self.spinBox.text()


	
	def actualizar(self):
		"""palabra=self.lineEdit.text()
		self.label.setText(palabra)"""
		palabra=""
		self.label.setText(palabra)
		palabrilla=self.lineEdit.text()
		self.lineEdit.setText(palabrilla.upper())
		self.label_2.setText("")

	def temporal(self):
		self.my_qtimer2 = QtCore.QTimer(self)
		self.my_qtimer2.timeout.connect(self.temporal2)
		self.my_qtimer2.start(1000)

	def temporal2(self):
					
		if self.tiempo>=-1:
			
			self.lcdNumber_2.display(self.tiempo)
			self.tiempo=self.tiempo-1
			if self.tiempo==-1:
				self.tiempo=int(self.nivel)
				self.actualizar()

	def reiniciar(self):
		self.incorrectas=0
		self.correctas=0
		self.puntaje=0
		self.lcdNumber.display(self.puntaje)
		self.lcdNumber_3.display(self.correctas)
		self.lcdNumber_4.display(self.incorrectas)
		self.label_2.setText("")
		self.lineEdit.setFocus()
	
	def evaluar(self):
		if self.lineEdit.text()==self.deuchland:
			self.label_2.setText("correcto")
			self.puntaje=self.puntaje+10*int(self.nivel)
			self.lcdNumber.display(self.puntaje)
			self.lcdNumber_3.display(self.correctas)
			self.correctas=self.correctas+1
		else:
			self.label_2.setText("incorrecto, debiste poner: "+self.deuchland)
			self.puntaje=self.puntaje-5*int(self.nivel)
			self.lcdNumber.display(self.puntaje)
			self.lcdNumber_4.display(self.incorrectas)
			self.incorrectas=self.incorrectas+1
		self.actualizar2()
		self.lineEdit.setText("")

	def actualizar2(self):
		self.level()

		palabra=""
		for x in range(0,int(self.nivel)):
			palabra=palabra+self.generarLetra()
		
		self.label.setText(palabra)
		self.deuchland=palabra
		self.tiempo=int(self.nivel)
		self.lineEdit.setFocus()

	def timer_start(self):

		self.my_qtimer = QtCore.QTimer(self)
		self.my_qtimer.stop()
		self.my_qtimer.timeout.connect(self.actualizar)
		self.my_qtimer.start(1000)
	
	def stop_timer(self):
		palabra=""
		self.my_qtimer.stop()
	
	def generarLetra(self):
		M=randint(1,27)
		if M ==1:
			LETRA="Q"
		if M ==2:
			LETRA="W"
		if M ==3:
			LETRA="E"
		if M ==4:
			LETRA="R"
		if M ==5:
			LETRA="T"
		if M ==6:
			LETRA="Y"
		if M ==7:
			LETRA="U"
		if M ==8:
			LETRA="I"
		if M ==9:
			LETRA="O"
		if M ==10:
			LETRA="P"
		if M ==11:
			LETRA="A"
		if M ==12:
			LETRA="S"
		if M ==13:
			LETRA="D"
		if M ==14:
			LETRA="F"
		if M ==15:
			LETRA="G"
		if M ==16:
			LETRA="H"
		if M ==17:
			LETRA="J"
		if M ==18:
			LETRA="K"
		if M ==19:
			LETRA="L"
		if M ==20:
			LETRA="Ñ"
		if M ==21:
			LETRA="Z"
		if M ==22:
			LETRA="X"
		if M ==23:
			LETRA="C"
		if M ==24:
			LETRA="V"
		if M ==25:
			LETRA="B"
		if M ==26:
			LETRA="N"
		if M ==27:
			LETRA="M"
		return LETRA
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
    
