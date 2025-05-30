#Ejercicio 1
'''
diccionario = {'nombre': 'Villa Sol', #key = "nombre" y el valor del key es "Villa Sol"
               "numero_de_estrellas": 5, 
               "habitaciones" :[ #key = "habitaciones" y su valor va hacer una listadentro de la lista va haber un diccionario 
                   {"numero": 5, "piso":1, "precio_por_noche": 60},#key = "numero" valor = 5
                    {"numero": 3, "piso": 2, "precio_por_noche": 62}] }
print(diccionario)
'''

'''
#Ejercicio 2
list_key = ['cat or dog', 'color', 'breed']
list_value = ["cat", "black", "angora"]

#creamos el diccionario dict
#el zip para emparejar las listas 
my_dict = dict(zip(list_key, list_value))

print(my_dict)
'''

#ejercicio 3
data = {"name": "Ana",
        "ID": "123456",
        "Age": "27",
        "email": "ana123@gmail.com"
        }\
    
list = ["email", "age "] #pasamos los key que queremos eliminar 

for i in list:
    if i in data:
        del data["Age"] #eliminamos el kay que queramos eliminar del diccionario

print(data)  

