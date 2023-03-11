print("Programa que determina numeros pares o impares \n")

num = int(input("Digite un numero: "))


#Se usan condicionales para validar que el modulo del numero coincida con alguno de los casos
if num % 2 == 0 :
    print("El numero", num, "es un numero par")
elif num % 2 == 1 :
    print("El numero", num, "es un numero impar")

#Excepcion si no es ningun numero con las caracteristicas de las condicionales
else:
	print("El numero no existe")