#ejercicio 1
""""
print('hello' + "world")
print("hello " + str(5))
print(str(5) + "world")
print([1,2] + [8,4])
print("house" + str(8))
print(6.7 + 5)
print(True + False)
"""

#ejercicio 2
'''
2. Cree un programa que le pida al usuario su nombre, apellido, 
y edad, y muestre si es un bebé, niño,preadolescente, adolescente, 
adulto joven, adulto, o adulto mayor.

name = input("Enter your name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

# Classifying age
if 0 <= age <= 2:
    print("User", name, "is a baby because they are", age, "years old.") 

elif 3 <= age <= 10:
    print("User", name, "is a child because they are", age, "years old.")

elif 11 <= age <= 12:
    print("User", name, "is a preadolescent because they are", age, "years old.")

elif 13 <= age <= 18:
    print("User", name, "is a teenager because they are", age, "years old.")

elif 19 <= age <= 29:
    print("User", name, "is a young adult because they are", age, "years old.")

elif 30 <= age <= 64:
    print("User", name, "is an adult because they are", age, "years old.")

else:
    print("User", name, "is an older adult because they are", age, "years old.")

'''

#ejercicio 3
'''
Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.

import random 
secret_num = random.randint(1, 10)
num= int(input("enter a number between 1 and 10"))

while num != secret_num:
    if secret_num < num:
        print("Incorrecvt, the secret number is smaller")
    else: 
        print("Incorrect, the secret number is larger")

    num= int(input("enter a number between 1 and 10"))

print("Bingo, you guessed it")
'''

#ejercicio 4
'''
num1 = int(input("enter a number "))
num2 = int(input("enter a number "))
num3 = int(input("enter a number "))

if num1 > num2 and num1 > num3:
    print("The largest number between the three is: ", num1)

if num2 > num1 and num2 > num3:
    print("The largest number between the three is: ", num2)

if num3 > num1 and num3 > num2:
    print("The largest number between the three is: ", num3)
'''


#jercicio #5
contador_de_nota = 1
cantidad_de_notas_aprobadas = 0
cantidad_de_notas_desaprobadas = 0
promedio_de_notas_aprobadas = 0
promedio_de_notas_desaprobadas = 0 

total_de_notas = int(input("Ingrese la cantidad de notas: "))

while contador_de_nota <= total_de_notas:
    nota_actual = int(input(f"Ingrese la nota número {contador_de_nota}: "))
    
    if nota_actual < 70:
        cantidad_de_notas_desaprobadas += 1
        promedio_de_notas_desaprobadas += nota_actual
    else:
        cantidad_de_notas_aprobadas += 1
        promedio_de_notas_aprobadas += nota_actual

    promedio_de_notas_total += nota_actual
    contador_de_nota += 1

if cantidad_de_notas_aprobadas > 0:
    promedio_de_notas_aprobadas /= cantidad_de_notas_aprobadas

if cantidad_de_notas_desaprobadas > 0:
    promedio_de_notas_desaprobadas /= cantidad_de_notas_desaprobadas

if total_de_notas > 0:
    promedio_de_notas_total /= total_de_notas

print("El estudiante tiene esta cantidad de notas aprobadas:", cantidad_de_notas_aprobadas)
print("Este es el promedio de notas aprobadas:", promedio_de_notas_aprobadas)

print("El estudiante tiene esta cantidad de notas desaprobadas:", cantidad_de_notas_desaprobadas)
print("Este es el promedio de notas desaprobadas:", promedio_de_notas_desaprobadas)

print("Este es el promedio total de notas:", promedio_de_notas_total)
