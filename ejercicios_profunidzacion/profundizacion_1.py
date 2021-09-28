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

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''
# Ingreso de Operadores string
texto_1 = input('Ingrese primero operador (ejemplo 2.1, 5) \n')
texto_2 = input('Ingrese segundo operador (ejemplo 2.1, 5) \n')

# Convierte string a float
numero_1 = float(texto_1)
numero_2 = float(texto_2)
# Ingreso de Operacion
operacion = input('ingrese operacion (Suma=+,Resta=-,Multiplicacion=*,Division=/,Exponenciacion=**)  \n')
oper = ""
if (operacion == '+'):
  oper = "Suma"  
elif (operacion == '-'):
    oper = "Resta"  
elif (operacion == '*'):
    oper = "Multiplicacion"  
elif (operacion == '/'):
    oper = "Division"
elif (operacion == '**'):   
    oper = "exponenciancion"   

# Calculo
resultado = 0.0
if (operacion == '+'):
  resultado = (numero_1 + numero_2)  
elif (operacion == '-'):
    resultado = (numero_1 - numero_2)  
elif (operacion == '*'):
    resultado = (numero_1 * numero_2)  
elif (operacion == '/'):
    resultado = (numero_1 / numero_2)  
elif (operacion == '**'):   
    resultado = (numero_1 ** numero_2)   

print('la', oper, ' entre ', numero_1, ' y ', numero_2, ' es ', resultado )

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio