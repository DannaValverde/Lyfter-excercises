'''
def hello_world():
    print("hello world")
    print("mi primera funcion")

hello_world()
'''

'''
#example parameter
def print_parameter (parameter_1, parameter_2, parameter_3):
    print(f'This is parameter 1 {parameter_1}')
    print(f'This is parameter 2: {parameter_2}')
    print(f'This is parameter 3: {parameter_3}')

#aca estan los valores de los parameter. el valor del parametro va segun su orden separado por comas. 
print_parameter(50, "hello", True) 

#Podemos cambiar los datos de los parametros sin perder los anteriores 
print_parameter([1,2,3], "23", "hola")


#parametros por defecto o sea ya tienen un valor establecido 
#Aca estamos estableciendo que el parametro 3 en el caso que no se le asigne ningun valor va a tener el valor de 3
#pero si le establecemos un valor como aca que es "True" no hay nigun problema a la hora de ejecutar su valor va hacer "True".
def print_parameter (parameter_1, parameter_2, parameter_3 = "2"):
    print(f'This is parameter 1 {parameter_1}')
    print(f'This is parameter 2: {parameter_2}')
    print(f'This is parameter 3: {parameter_3}')

print_parameter(50, "hello", True) 
'''

'''
#funcion que optenga el promedio (sumatoria de las materias /3)

def get_avarage_score(score): #el parametro score va hacer un espacio libre ya que funciona como un input para recibir las notas de los diccionarios
    return (score["spanish_score"] + score["science_score"] + score["history_score"]) /3 

#Funcion que verifique si el estudiante se eximio o no 

def is_student_exempted(score):
    return score["average_score"] > 70

#los diccionarios de las notas de los estudiantes

juan_score = {
     "Spanish_score": 34,
    "science_score" : 66,
    "history_score": 87,
}


maria_score = {
     "Spanish_score": 34,
    "science_score" : 66,
    "history_score": 87,
}

paul_score = {
    "Spanish_score": 99,
    "science_score" : 88,
    "history_score": 77,
}

juan_score['average_score'] = get_avarage_score(juan_score) #aca creamos una lista temporal para guardar los datos en avarage_score
maria_score['average_score'] = get_avarage_score(maria_score)
paul_score['average_score'] = get_avarage_score(paul_score)

juan_score["is_exempted"] = is_student_exempted(juan_score)
maria_score["is_exempted"] = is_student_exempted(maria_score)
paul_score["is_exempted"] = is_student_exempted(paul_score)

'''

#codigo minimizado 

def get_average_score(scores):
  return (scores["spanish_score"] + scores["science_score"] + scores["history_score"]) / 3


def is_student_exempted(scores):
  return scores["average_score"] > 70


# Scores
students = [
  {
    "name": "Juan",
		"spanish_score": 75,
		"science_score": 95,
		"history_score": 54,
	},
  {
    "name": "Sofia",
		"spanish_score": 64,
		"science_score": 56,
		"history_score": 98,
	},
  {
    "name": "Paul",
		"spanish_score": 72,
		"science_score": 75,
		"history_score": 79,
	}
]

# Averages
#va  a psar por cada estuidnate o sea por cada diccionario. 
# lo que hace que basicamente es una lista con diccionario adentro 
for student in students:
  student["average_score"] = get_average_score(student)
  student["is_exempted"] = is_student_exempted(student)
  print(student["name"], " is_exempted is ", student["is_exempted"])

#recordar que cuando queremos accesar a cosas especificas de una lista usamos [ ]

#parametro --> input
#return --> output