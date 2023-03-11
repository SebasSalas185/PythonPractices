#Programa para determinar el numero mas grande introducido por el usuario

#Peticion de 3 numeros enteros por pantalla
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))
num3 = int(input("Introduce el tercer numero: "))

#Condicional en caso de que num1 fuera el mayor
if num1 > num2 and num1 > num3:
	print("\nEl numero", num1, "es el numero mas grande de los tres")

#Condicional en caso de que num2 fuera el mayor 
elif num2 > num1 and num2 > num3:
	print("\nEl numero", num2, "es el numero mas grande de los tres")

#Condicional en caso de que num3 fuera el mayor 
elif num3 > num1 and num3 > num2:
	print("\nEl numero", num3, "es el numero mas grande de los tres") 	