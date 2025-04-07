
import json 

with open("C:/Users/Danna/Documents/lyfter/pokemons.json", "r") as archivo:  #aqui abrimos el documento pokemons.json para leerlo (direccion del documento pokemons.json)
    new_data = json.load(archivo)  #aca pasamos el documento a python 

#los datos para el nuevo pokemon 
name = input("entender the name of the new pokemon")
kind = input("enter the type of pokemon")

hp = int(input("enter the hp"))
attack = int(input("enter the type of attack"))
defense= int(input("enter the type of defense"))
sp_Attack= int(input("enter the sp.Attack number"))
sp_Defense = int(input("enter the sp.Defense number "))
speed=input("enter the speed")

#aqui guardamos en un diccionario los datos del nuevo pokemon
new_Pokemon = {
    "name:" : {"english": name},
    "kind" :[kind],
    "base": {
        "hp" : hp,
        "attack" : attack,
        "defense" : defense,
        "Sp.attack" : sp_Attack,
        "sp.Defense" : sp_Defense,
        "speed" : speed
    }
}


new_data.append(new_Pokemon) # agregamos los datos de new pokemons a newData 

#volvemos abrir el documento json pero ahora para escribir
with open("C:/Users/Danna/Documents/lyfter/pokemons.json", "w") as archivo:
    json.dump(new_data,archivo, indent=4)  #aca pasamos los datos del dicionario new_pokemon a json 


print("C:/Users/Danna/Documents/lyfter/pokemons.json")