phrase = input("Escriba una frase: ") 
#Peticion por terminal de una frase al usuario 

word = input("\nEscriba una palabra de la frase introducida que quiere eliminar: ") 
#Peticion por terminal de una palabra de la cadena que se quiera eliminar

position = phrase.find(word) 
#Variable que busca la cadena ingresada de "word" en "phrase"

quitespace = len(word) + 1 
#Variable que guarda la longitud de la cadena "word" mas 1 (que simboliza un caracter de espacio)

subphrase = phrase[0 : position] + phrase[position + quitespace: ] 
#La variable guarda un substring de la cadena de "phrase" desde su posicion "0" hasta "word" en "phrase".
#La variable guarda un substring de la concatenacion de "position y quitespace" hasta el "final de la cadena".
#La variable concatena los 2 substrings y forma la nueva frase sin la cadena "word" en "phrase"


print(f"La frase sin esa palabra seria: {subphrase}")
#Mostrar en pantalla la frase con la cadena eliminada