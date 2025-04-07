#Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
#1. Suma
#2. Resta
#3. Multiplicación
#4. División
#5. Borrar resultado
#Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
#Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.

def mostrar_menu():
    print("\nMenu de operaciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Borrar resultado")
    print("6. Salir")

def calculadora():
    numero_actual = 0
    
    while True:
        print(f"Numero actual: {numero_actual}")
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opcion: "))
            
            if opcion == 6:
                print("Saliendo del programa")
                break
            
            if opcion < 1 or opcion > 6:
                print("Opcion invalida, intente de nuevo.")
                continue

            if opcion == 5:
                numero_actual = 0
                print("Resultado borrado")
                continue

            nuevo_numero = float(input("Ingrese el nuevo número: "))
            
            if opcion == 1:
                numero_actual = nuevo_numero + numero_actual
            elif opcion == 2:
                numero_actual = nuevo_numero - numero_actual
            elif opcion == 3:
                numero_actual = nuevo_numero * numero_actual
            elif opcion == 4:
                if nuevo_numero == 0:
                    print("Error. division por cero no es psible")
                else:
                    numero_actual = nuevo_numero / numero_actual
            else:
                print("Opcion invalida. Intenta de nuevo.")
        
        except ValueError:
            print("Entrada invalida, por favor, ingresa un numero valido.")

#Nota: usualmente cuando hacemos una operacion en la calculadora, ingresa un numero y luego aparece el menú
# para que elija que hacer con ese numero. Asi cd vez que se ingrese un numero, el menu vuelve a salir para
# que decida la siguiente operacion a realizar con el resultado actual.

#inicio de la calculadora 
if __name__ == "__main__":
    calculadora()