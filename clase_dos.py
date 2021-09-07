# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 19:03:51 2021

@author: Maria Camila
"""
# Condicionales

# Tabla de verdad

# Tabla del AND
# v and v = v
# v and f = f
# f and v = f
# f and f = f

print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# Tabla del or
# v or v = v
# v or f = v
# f or v = v
# f or f = f

print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# Negacion

print(not True)  # False
print(not False)  # True

# Mas de dos condiciones al mismo tiempo
print(True and False and True or False or True or True)  # True
print(True and (False and True) or False or (True or True))  # True

# Jerarquia de operaciones
# 1. Parentesis y llaves
# 2. Potencias y llaves
# 3. Multiplicacion y division
# 4. Sumas y Restas

# Jerarquia de operaciones booleanas
# 1. Parentesis y llaves
# 2. Tabla de verdad

# Estructura if
x = 1
if (x > 0):
    print('1')
else:
    print('2')
    print('3')

# Haga un algoritmo que dada la edad de una persona indique si es mayor o menor
# de edad

edad = int(input('Digite su edad: '))
if(edad >= 18):
    print('Es mayor de edad')
else:
    print('Es menor de edad')

# Haga un algoritmo que indique si un estudiante aprobo o reprobo una
# asignatura teniendo en cuenta que aprueba con minimo una calificacion de 3.0
# hasta 5.0. EL rango válido de la nota debe ser entre 0 y 5.
nota = float(input('Digite la nota: '))
if(nota >= 3 and nota <= 5):
    print('Usted aprobó la materia. ')
elif(nota < 3 and nota > 0):
    print('Usted reprobó la materia.')
else:
    print('La nota ingresada no es válida.')

# Haga un algoritmo que dado un número n diga si es negativo, positivo o cero.
número = float(input('Digite un número: '))
if(número > 0):
    print('El número es positivo. ')
elif(número < 0):
    print('El número es negativo. ')
else:
    print('El número es cero.')

# Ciclos
# Ciclo for
for valor in range(11):
    print(valor)
for valor in range(1, 11):
    print(valor)
for valor in range(2, 11, 2):
    print(valor)

for valor in range(11):
    print(valor)
    print(valor + 1)

# Haga un algoritmo que de las n notas de un estudiante y calcule el promedio
# académico final.

numero_notas = int(input('Digite cuantas notas va a promediar: '))
if(numero_notas > 0):
    suma = 0
    for x in range(numero_notas):
        calificación = float(input(f'Digite la nota {x + 1}: '))
        suma = suma + calificación
    promedio = suma / numero_notas
    promedio = round(promedio, 2)
    print(f'El promedio final es: {promedio}')
else:
    print('El número de notas no puede ser menor o igual a cero. ')
