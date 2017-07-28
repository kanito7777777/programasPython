#encoding: utf8
#1 = jugador persona
#-1 = jugador maquina
#0 = vacio

import random

def mostrar(M):
	for i in M:
		for j in i:
			if j == 0:
				print "_\t",
			elif j == 1:
				print "X\t",
			else:
				print "0\t",
		print

def jugarPersona(M):
	i = input("Ingrese Fila: ")
	j = input("Ingrese Columna: ")
	if i > 2 or j > 2:
		print "-----Fuera de Rango, elija otra!!!"
		jugarPersona(M)
	elif M[i][j] == 0:
		M[i][j] = 1
	else:
		print "-----Esa posicion ya esta ocupada, elige otra!!!"
		jugarPersona(M)	

def jugarMaquina(M):
	i = random.randint(0, 2)
	j = random.randint(0, 2)
	if M[i][j] == 0:
		M[i][j] = -1
	else:
		jugarMaquina(M)

def verificarEmpate(M):
	listaAux = []
	listaAux.extend(M[0])
	listaAux.extend(M[1])
	listaAux.extend(M[2])
	return listaAux.count(0)

def contarFila(M, dato):
	return M[0].count(dato) == 3 or M[1].count(dato) == 3 or M[2].count(dato) == 3

def verificarGanador(M):
	ganaPersona = False
	ganaMaquina = False

	#verificando ganadores filas
	ganaPersona = contarFila(M, 1)
	ganaMaquina = contarFila(M, -1)

	if ganaPersona:
		print "Felicidades!!! Ganaste"
		return True
	if ganaMaquina:
		print "Perdiste!!! =("
		return True
	
	#verificando columnas
	matrizAux = []
	for i in xrange(0,3):
		listaCol = []
		for j in xrange(0,3):
			listaCol.append(M[j][i]) 
		matrizAux.append(listaCol)

	ganaPersona = contarFila(matrizAux, 1)
	ganaMaquina = contarFila(matrizAux, -1)

	if ganaPersona:
		print "Felicidades!!! Ganaste"
		return True
	if ganaMaquina:
		print "Perdiste!!! =("
		return True

	#verificando diagonales
	matrizAux = []
	listaCol = []
	for i in xrange(0,3):
		listaCol.append(M[i][i])
	matrizAux.append(listaCol)
	
	listaCol = []
	for i in xrange(0,3):
		listaCol.append(M[i][2-i]) 
	matrizAux.append(listaCol)

	ganaPersona = matrizAux[0].count(1) == 3 or matrizAux[1].count(1) == 3
	ganaMaquina = matrizAux[0].count(-1) == 3 or matrizAux[1].count(-1) == 3

	if ganaPersona:
		print "Felicidades!!! Ganaste"
		return True
	if ganaMaquina:
		print "Perdiste!!! =("
		return True

	#verificando empate
	if verificarEmpate(M) == 0:
		print "Empate!!!!!"
		return True

	return False
		
matriz =[[0,0,0],[0,0,0],[0,0,0]]

while True:
	mostrar(matriz)
	jugarPersona(matriz)
	
	if verificarGanador(matriz):
		break

	jugarMaquina(matriz)
	if verificarGanador(matriz):
		break

print "======= RESULTADO FINAL ======="
mostrar(matriz)