

#1. Cree un programa que lea nombres de canciones de un archivo (línea por línea) y 
# guarde en otro archivo los mismos nombres ordenados alfabéticamente.

     
def readFile(songs):
    with open(songs) as file:
        lines = file.readlines()

    lines.sort() #orden alfabetico de la lista line 

    #Este archivo se crea automáticamente si no existe.
    with open('newFile.txt', 'w') as newFile:
        newFile.writelines(lines) 
    #Todas las lineas escritas en la lista lines las vamos a guardar o escribir en el archivo newFile por eso usamos en el modo ("w") ya que vamos a reescribir en este newFile

    with open('newFile.txt', 'r') as newFile: #ahora el modo es ("r") por que ahora vamos abirir el archivo pero para leerlo ya que ya se abrio para escribirlo
        for line in newFile:
            print(line)  

readFile('C:/Users/Danna/Documents/lyfter/Canciones.txt') #Aca pasamos el valor o direccion al parametro songs
#songs es igual a canciones.txt por que al final de la funcion estamos agregando el valor del parametro que es la ubicacion del archivo.

#Notas:
#en la primera abrimos el archivo para guardar el archivo en la variable file y cuando se abre se guardar los datos de file en la lista lines y las ordena alfabeticamente
#en la segunda vez se abre como un modo "w" que es para escribir en el nuevo archivo los datos que trae la lista lines(que son las canciones) despoues se cierra
#y la tercera vez se abre el archivo newFile pero ahora con un modo de ("r") ya que vamos a leer los datos yta guardados anteriormente y los vamos a procesar linea por line#a



    



