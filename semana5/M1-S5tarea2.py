#ejercicio 1
'''
first_list = ["Hay", "casas", "bonitas", "en "]
second_list = ["algunos", 'barrios', 'de','San Jose']

for i in range(len(first_list)):
    print(f'{first_list[i]} {second_list[i]}')
'''

#segundo ejercicio 
'''
my_string = 'Hola Mundo'

for i in range(len(my_string) - 1,-1,-1):  # Desde el último índice hacia el primero
    print(my_string[i])
'''

#tercer ejercicio 
'''
my_list = [8, 4, 2, 11, 3]

# Intercambiamos el primer y el último elemento
my_list[0], my_list[-1] = my_list[-1], my_list[0]

print(my_list)      
'''

#cuarto ejercicio
'''
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]  
pares_list = []  # Lista para almacenar los números pares

for num in my_list:
    if num % 2 == 0: 
        pares_list.append(num)  # Agregamos el número par a la nueva lista

print(pares_list) 
'''

#quinto ejercicio 
numeros = []

for i in range(10):
    num = int(input(f'ingrese el numero {i+1}: '))
    numeros.append(num)

print(f'Los numeros ingresados son: {numeros}')

max_num = max(numeros)

print(f'El numero mas altp fue: {max_num}')
    