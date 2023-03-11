#Programa que suma X con Y hasta que Y = 1597, guardando sus resultados mutuamente hasta llegar a la meta

x, y = 0, 1 	
#Bucle que concluye cuando y sea mayor o igual a 1597
while y <= 1597:
	#Print que imprime variable X y Y, end para no saltar de linea
	print(x, y, end = " ")
	#Primera suma X con Y y se guarda en X 
	x += y
	#Con la anterior suma ya guardada en X, se suma con Y 
	y += x