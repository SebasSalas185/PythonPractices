#Una calculadora que contiene operaciones tales como: Suma, Resta, Multiplicacion, Division, Exponentes, Modulo Y Division Entera

print("Calculadora \n")
print("Operadores: (+) (-) (*) (/) (**) (%) (//)\n")

num = int(input("Digite el primer numero entero usado de la operacion: "))
#Peticion de un numero entero para operacion
sig = input("\nDigite el operador usado de la operacion: ")
#Peticion del signo que se ocupa en la operacion

#Condicional del caso que sea suma
if sig == "+":
	num += int(input("\nElegiste sumar, digite el sumando: "))
	print("\nLa suma da como resultado:", num)

#Condicional del caso que sea resta
elif sig == "-":
	num -= int(input("\nElegiste restar, digite el sustraendo: "))
	print("\nEl resto es:", num)

#Condicional del caso que sea multiplicacion
elif sig == "*":
	num *= int(input("\nElegiste multiplicar, digite el multiplicador: "))
	print("\nEl producto es:", num)

#Condicional del caso que sea division
elif sig == "/":
	num /= int(input("\nElegiste dividir, digite el divisor: "))
	print("\nEl cociente es:", num)

#Condicional del caso que sea exponente
elif sig == "**":
	num **= int(input("\nElegiste exponencial, digite el exponente : "))
	print("\nEl producto exponencial es:", num)

#Condicional del caso que sea modulo
elif sig == "%":
	num %= int(input("\nElegiste el modulo, digite el otro modulo: "))
	print("\nEl resultado del modulo es:", num)

#Condicional del caso que sea division entera
elif sig == "//":
	num //= int(input("\nElegiste dividir enteros, digite el divisor: "))
	print("\nEl cociente entero es:", num)

#Excepcion si no se cumple ninguna condicional
else:
	print("\nLo sentimos, la operacion con ese operador no esta disponible")