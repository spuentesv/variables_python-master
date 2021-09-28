# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella
print('Ingrese palabra 1 (Longitud 10 letras):')
palabra_1 = str(input())

print('Ingrese palabra 2 (Longitud 10 letras):')
palabra_2 = str(input())

# De la primera palabra tome las primeras tres letras, utilice el operador :
resultado1 = ''
if len(palabra_1.strip()) > 0:
    resultado1 = palabra_1[0] + palabra_1[1] + palabra_1[2]
print('primera palabra', palabra_1, ' 3 letras iniciales ', resultado1)        

# De la segunda palabra tome las primeras dos letras, utilice el operador :
resultado2 = ''
if len(palabra_2.strip()) > 0:
    resultado2 = palabra_2[0] + palabra_2[1]
print('primera palabra', palabra_2, ' 2 letras iniciales ', resultado2)        

# Formar una nueva palabra con los recortes solicitados
resultado = resultado1 + resultado2
print('genera la palabra', resultado)        


# Imprima en pantalla los resultados
