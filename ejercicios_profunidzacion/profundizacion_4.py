# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica numérica y cadenas
'''
Enunciado:
Realice un programa que determine cual sería el apellido de una persona
al ingresara los dos nombres completos de sus padres.
En definitiva se solicita crear una variable nueva que reuna
los apellidos.

- Primero el programa debe consultar el nombre completo del padre_1
- Luego el programa debe consultar el nombre completo del padre_2
- Luego debe consultar el nombre del hijo/a
- Debe extraer los apellidos de los padres (ver la nota al final)
- Luego formar el nombre completo del hijo/a utilizando los apellidos
  de sus padres y el nombre ingresado de dicha persona
- Imprimir en pantalla el resultado

NOTA: Para extraer el apellido del nombre completo recomendamos usar
el método "split"
Mostraremos un ejemplo:

direccion_completa = 'Monroe 2716'
calle, altura = direccion_completa.split(' ')

Les dejo por su cuenta a que busquen un poco más acerca de este método
que seguramente utilizarán mucho de acá en adelante.
Les dejamos un link con algunos ejemplos más:
https://www.pythonforbeginners.com/dictionary/python-split

Cualquier duda con el método split pueden consultarla por el campus
'''
# Ingreso de Operadores string
texto_1 = input('Ingrese Nombre completo Padre(Nombre1 Nombre2 Apellido Paterno Apellido Materno)   : \n')
texto_2 = input('Ingrese Nombre completo Madre(Nombre1 Nombre2 Apellido Paterno Apellido Materno)   : \n')
texto_3 = input('Ingrese Nombre hijo(a)  (Nombre1 Nombre2)                                          : \n')

padre = texto_1.split(" ")
madre = texto_2.split(" ")


# Imprime datos ingresados
#print('Nombre Completo: ', padre)
#print('Nombre Completo: ', madre)
print('Nombre hijo: ', texto_3, padre[2], madre[2],)



print('Jugando con texto')
# Empezar aquí la resolución del ejercicio
