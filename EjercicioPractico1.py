#Sistema que determina por medio de una clave y años en la empresa, de cuanto sera el periodo vacacional

print("Bienvenido a la calculadora de periodo de vacaciones \n")

nom = input("Cual es su nombre?: ") 
passu = int(input("Digite su clave: "))

pass1 = 3132
pass2 = 4142
pass3 = 6913

if passu != pass1 and passu != pass2 and passu != pass3:
    print("La clave ingresada no coincide con ninguno de los departamentos")
else:
    print(f"\nBienvenido, {nom}")

if passu == pass1 :
	print(f"\nUsted pertenece al departamento de servicio al cliente\n")
	
	ressc = int(input(nom + ", introduzca la cantidad de años que lleva trabajando en esta empresa: "))
	if ressc == 1 :
		print("\n" + nom + ", usted tiene derecho a recibir 6 dias de vacaciones en servicio al cliente")
	elif ressc != 1:
		if ressc < 7:
			print("\n" + nom + ", usted tiene derecho a recibir 14 dias de vacaciones en servicio al cliente")
		elif ressc >= 7 :
	 		print("\n" + nom + ", usted tiene derecho a recibir 20 dias de vacaciones en servicio al cliente")
	


if passu == pass2 :
	print(f"\nUsted pertenece al departamento de logistica\n")
	
	resl = int(input(nom + ", introduzca la cantidad de años que lleva trabajando en esta empresa: "))
	if resl == 1 :
		print("\n" + nom + ", usted tiene derecho a recibir 7 dias de vacaciones en logistica")
	elif resl != 1:
		if resl < 7:
			print("\n" + nom + ", usted tiene derecho a recibir 15 dias de vacaciones en logistica")
		elif resl >= 7 :
	 		print("\n" + nom + ", usted tiene derecho a recibir 22 dias de vacaciones en logistica")


if passu == pass3 :
	print(f"\nUsted pertenece al departamento de gerencia\n")
	
	resg = int(input(nom + ", introduzca la cantidad de años que lleva trabajando en esta empresa: "))
	if resg == 1 :
		print("\n" + nom + ", usted tiene derecho a recibir 10 dias de vacaciones en gerencia")
	elif resg != 1:
		if resg < 7:
			print("\n" + nom + ", usted tiene derecho a recibir 20 dias de vacaciones en gerencia")
		elif resg >= 7 :
	 		print("\n" + nom + ", usted tiene derecho a recibir 30 dias de vacaciones en gerencia")