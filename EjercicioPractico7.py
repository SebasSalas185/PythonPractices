palabra = input("Escriba una cadena de caracteres: ")
#Se pide por pantalla una cadena de caracteres

inversa = ""
#Variable llamada "inversa" que almacenara la cadena invertida

for cadena in palabra:
    #bucle for para almacenar cada caracter de "palabra" en la variable "cadena"
    inversa = cadena + inversa
    #Concatenacion de variables "cadena" e "inversa", 
    #Guarda todos los caracteres de forma inversa gracias al orden de concatenacion  

print("La cadena es:", palabra)
#Imprimir "palabra" para mostrar la entrada del usuario
print("La cadena a la inversa es :", inversa)  
#Imprimir "inversa" para mostrar el resultado de invertir la entrada del usuario