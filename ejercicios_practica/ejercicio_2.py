# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica y consola

# Ahora los valores a operar deben ser ingresados por
# consola con la función "input" como se ve a continuación
print('Ingrese por consola el primer número decimal a operar:')
numero_1 = int(input())

print('Ingrese por consola el segundo número decimal a operar:')
numero_2 = int(input())

# Alumno: Imprima en pantalla los dos números decimales solicitados
# print(....)
print('Se ingresaron los siguientes numeros', numero_1, ' y ', numero_2)

# Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
# numero_1, numero_2
# Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
# El resultado de sumar 4 y 2 es 6
# NOTA: No coloque usted los nùmeros y resultados, use las variables

# Suma
resultado = numero_1 + numero_2
print('Se sumaron los siguientes numeros', numero_1, ' y ', numero_2, ' resultando ', resultado)
# Resta
resultado = numero_1 - numero_2
print('Se restaron los siguientes numeros', numero_1, ' y ', numero_2, ' resultando ', resultado)
# División
resultado = 0
if (numero_2 > 0):
    resultado = numero_1 / numero_2
print('Se dividieron los siguientes numeros', numero_1, ' y ', numero_2, ' resultando ', resultado)
# Multiplicación
resultado = numero_1 * numero_2
print('Se multiplicaron los siguientes numeros', numero_1, ' y ', numero_2, ' resultando ', resultado)
