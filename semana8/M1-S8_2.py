#Exercise 1
'''
first_list = ['hay', 'en', 'que','iteracion','indices', 'muy']
second_list = ['casos','los','la','por','es','util']


a_single_list = list(zip(first_list, second_list)) #une ambas listas
for palabra1, palabra2 in a_single_list: #combinamos ambas listas y con for las recorremos 
    print(palabra1, palabra2)
'''

#Exercise 2
'''
my_string = 'Pizza con pepperoni'

for i in range(len(my_string)-1,-1,-1):
    print(my_string[i])

#Con range podemos acceder a los indicies usando el cilo for nos ayuda a ir uno por uno pero de manera inversa gracias a que con len como esta en negativo los recorremos 1 por 1
'''

#Exercise 3
'''
my_list=[1,2,3,3,455,6]
if len(my_list) >= 2: #aca verifica el tama;o de la lista mientras hayan 2 valores en la lista:
    my_list[0],my_list[-1] = my_list [-1],my_list[0] #el ultimo vcalor va hacer el primero y diceversa
    print(my_list)
'''

#Exercise 4
'''
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for numero in my_list:
    if numero % 2 != 0:
        my_list.remove(numero)
print(my_list)
'''

#Exercise 5
numbers = []

for i in range(10):
    user_n = int(input(f"ingrese 10 numeros {i }: "))
    numbers.append(user_n)

numeroMayor = max(numbers)
print(numbers)
print(f"el numero mayor de los numerosa que ustd ingreso fue el: {numeroMayor}")
 

    


