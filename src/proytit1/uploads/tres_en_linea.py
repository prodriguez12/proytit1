# Integrante: Patricio Rodríguez Rojas
# Observaciones:
# Para evitar usar variables globales u otra complicacion de comunicacion entre las funciones 
# a_jugar() y tres_en_linea() se decidió imprimir los resultados por pantalla en la funcion
# tres_en_linea(). La funcion a_jugar() se encarga solo de una partida y retorna el
# resultado de dicha partida.


import turtle

#1.
def tablero(distancia=80):
	turtle.reset()
	turtle.degrees()
	turtle.penup()
	turtle.setpos(-distancia/2,distancia*3/2)
	turtle.pendown()
	turtle.right(90)
	turtle.forward(distancia*3)
	turtle.penup()
	turtle.left(90)
	turtle.forward(distancia)
	turtle.left(90)
	turtle.pendown()
	turtle.forward(distancia*3)
	turtle.penup()
	turtle.right(90)
	turtle.forward(distancia)
	turtle.right(90)
	turtle.forward(distancia)
	turtle.right(90)
	turtle.pendown()
	turtle.forward(distancia*3)
	turtle.penup()
	turtle.left(90)
	turtle.forward(distancia)
	turtle.left(90)
	turtle.pendown()
	turtle.forward(distancia*3)
	turtle.penup()
	turtle.setpos(-distancia, distancia)
	turtle.pendown()
	turtle.write("1",align="center")
	turtle.penup()
	turtle.setpos(0, distancia)
	turtle.pendown()
	turtle.write("2",align="center")
	turtle.penup()
	turtle.setpos(distancia, distancia)
	turtle.pendown()
	turtle.write("3",align="center")
	turtle.penup()
	turtle.setpos(-distancia,0)
	turtle.pendown()
	turtle.write("4",align="center")
	turtle.penup()
	turtle.setpos(0,0)
	turtle.pendown()
	turtle.write("5",align="center")
	turtle.penup()
	turtle.setpos(distancia,0)
	turtle.pendown()
	turtle.write("6",align="center")
	turtle.penup()
	turtle.setpos(-distancia, -distancia)
	turtle.pendown()
	turtle.write("7",align="center")
	turtle.penup()
	turtle.setpos(0, -distancia)
	turtle.pendown()
	turtle.write("8",align="center")
	turtle.penup()
	turtle.setpos(distancia, -distancia)
	turtle.pendown()
	turtle.write("9",align="center")
	turtle.penup()
	turtle.setpos(-distancia*3/2,-distancia*3/2)

#2.
def cruz(posicion,c,r,distancia=80):
	turtle.degrees()
	if posicion > 0 and posicion < 4:
		pos = turtle.setpos(distancia*(posicion-2),distancia-r)
	if posicion > 3 and posicion < 7:
		pos = turtle.setpos(distancia*(posicion-5),-r)
	if posicion > 6 and posicion < 10:
		pos = turtle.setpos(distancia*(posicion-8),-distancia-r)
	turtle.fillcolor("white")
	turtle.begin_fill()
	turtle.circle(r)
	turtle.end_fill()
	if c == 'r':
		turtle.pencolor("red")
	elif c == 'b':
		turtle.pencolor("blue")
	pos
	turtle.right(45)
	turtle.forward(r)
	turtle.right(180)
	turtle.pendown()
	turtle.forward(2*r)
	turtle.penup()
	turtle.right(180)
	turtle.forward(r)
	turtle.left(90)
	turtle.forward(r)
	turtle.left(180)
	turtle.pendown()
	turtle.forward(2*r)
	turtle.penup()
	turtle.right(225)
	turtle.setpos(-distancia*3/2,-distancia*3/2)

#3.
def circulo(posicion,c,r,distancia=80):
	turtle.degrees()
	turtle.fillcolor("white")
	if posicion > 0 and posicion < 4:
		turtle.setpos(distancia*(posicion-2),distancia-r)
	elif posicion > 3 and posicion < 7:
		turtle.setpos(distancia*(posicion-5),-r)
	elif posicion > 6 and posicion < 10:
		turtle.setpos(distancia*(posicion-8),-distancia-r)
	if c == 'r':
		turtle.pencolor("red")
	elif c == 'b':
		turtle.pencolor("blue")
	turtle.pendown()
	turtle.begin_fill()
	turtle.circle(r)
	turtle.end_fill()
	turtle.penup()
	turtle.setpos(-distancia*3/2,-distancia*3/2)

#4.
def a_jugar(partida):
	tablero()
	marcador = ["V"]*9
	victoria = 0
	if partida%2 == 1:
		colores = ['r','b']
		jugador = 0
	else:
		colores = ['b','r']
		jugador = 1
	
	while victoria == 0 and "V" in marcador:
		jugar = input("(jugador "+str(jugador%2 + 1)+", partida "+str(partida)+") Ingrese jugada: ")
		jugada = int(jugar)
		if jugada < 1 or jugada > 9:
			print("No existe esa jugada.")
			jugada = scan("(jugador "+str(jugador%2 + 1)+", partida "+str(partida)+") Ingrese jugada: ")
		if "V" in marcador[jugada-1] and jugador%2 == 0:
			circulo(jugada,colores[0],20,80)
			marcador[jugada-1] = "O"
		elif "V" in marcador[jugada-1] and jugador%2 == 1:
			cruz(jugada,colores[1],20,80)
			marcador[jugada-1] = "X"
		else:
			print("Jugada ya realizada!")
			jugada = scan("(jugador "+str(jugador%2 + 1)+", partida "+str(partida)+") Ingrese jugada: ")
		
		if jugada < 4:
			if marcador[jugada-1] == marcador[jugada+2] and marcador[jugada-1] == marcador[jugada+5]:
				victoria = jugador%2 + 1
			elif marcador[0] == marcador[1] and marcador[0] == marcador[2]:
				victoria = jugador%2 + 1
			elif jugada == 1:
				if marcador[0] == marcador[4] and marcador[0] == marcador[8]:
					victoria = jugador%2 + 1
			elif jugada == 3:
				if marcador[2] == marcador[4] and marcador[2] == marcador[6]:
					victoria = jugador%2 + 1
			
		elif jugada > 3 and jugada < 7:
			if marcador[jugada-1] == marcador[jugada-4] and marcador[jugada-1] == marcador[jugada+2]:
				victoria = jugador%2 + 1
			elif marcador[3] == marcador[4] and marcador[3] == marcador[5]:
				victoria = jugador%2 + 1
			elif jugada == 5:
				if marcador[0] == marcador[4] and marcador[0] == marcador[8]:
					victoria = jugador%2 + 1
				elif marcador[2] == marcador[4] and marcador[2] == marcador[6]:
					victoria = jugador%2 + 1
		
		elif jugada > 6:
			if marcador[jugada-1] == marcador[jugada-4] and marcador[jugada-1] == marcador[jugada-7]:
				victoria = jugador%2 + 1
			elif marcador[6] == marcador[7] and marcador[6] == marcador[8]:
				victoria = jugador%2 + 1
			elif jugada == 9:
				if marcador[0] == marcador[4] and marcador[0] == marcador[8]:
					victoria = jugador%2 + 1
			elif jugada == 7:
				if marcador[2] == marcador[4] and marcador[2] == marcador[6]:
					victoria = jugador%2 + 1
		jugador += 1
	if victoria == 1:
		return (3,0)
	elif victoria == 2:
		return (0,3)
	else:
		return (1,1)

#5.
def tres_en_linea(n):
	resultado = [0,0]
	for i in range(0,n):
		parcial = a_jugar(i+1)
		if n%2 == 1:
			resultado[0] = resultado[0] + parcial[0]
			resultado[1] = resultado[1] + parcial[1]
		else:
			resultado[0] = resultado[0] + parcial[1]
			resultado[1] = resultado[1] + parcial[0]
		
		print("Fin jugada: (jugador 1, jugador 2) = ("+str(resultado[0])+","+str(resultado[1])+")")
	print("--------------------------- FIN DEL JUEGO ---------------------------\n"+
		"JUGADOR 1: "+str(resultado[0])+"\n"+
		"JUGADOR 1: "+str(resultado[1]))
	if resultado[0] > resultado[1]:
		print("----------------------- FELICIDADES JUGADOR 1 -----------------------")
	elif resultado[1] > resultado[0]:
		print("----------------------- FELICIDADES JUGADOR 2 -----------------------")
	else:
		print("----------------------- FELICIDADES JUGADORES -----------------------")
