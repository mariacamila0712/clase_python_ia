# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 18:53:28 2021

@author: Maria Camila
"""

print('Hello World')

# Variables
a = 3
print(type(a))
a = "Hola"
print(type(a))
a = 3.5
print(type(a))
a = True
print(type(a))


# Operaciones

# Suma

a = 5
b = 2
c = a + b
print(c)


#  Resta

a = 5
b = 2
c = a - b
print(c)

# Multiplicacion

a = 5
b = 2
c = a * b
print(c)

# Division

a = 5
b = 2
c = a / b
print(c)

a = 5
b = 2
c = a // b
print(c)

# Potencia

a = 5
b = 2
c = a ** b
print(c)

# Raiz

a = 9
c = a ** (1/3)
print(c)

# import math
# raiz = math.sqrt(25)
# print(raiz)

# Tipos de datos

# String str
a = "Hola Mundo"
a = 'Hola Mundo'
b = "I can't do it"
c = 'Alias "Maria"'

# Entero int
a = 5

# Decimal float
a = 5.6

# Booleano bool
x = True
y = False

# Conversiones entre tipos de datos

# Convertir de x a entero

a = '3'
y = int(a)
print(y)
print(type(y))

# Convertir de x a decimal

a = '3'
y = float(a)
print(y)
print(type(y))

# Convertir de x a string

a = 3
y = str(a)
print(y)
print(type(y))

# Concatenaciones
a = 'hola'
b = 'mundo'
c = a + ' ' + b

# Capturar por pantalla
nombre = input('Digite su nombre: ')
print('Hola', nombre)

# Haga un algoritmo que sume dos numeros e imprima su resultado
d = float(input('Digite el primer numero: '))
e = float(input('Digite el segundo numero: '))
f = d + e
# print('La suma de los dos numeros es: ', f)
print(f'La suma de los numeros {d} + {e} es {f}')

# Haga un algoritmo que lea un numero y lo eleve al cuadrado

numero = int(input('Digite el numero que desea sacar la potencia: '))
potencia = numero ** 2
print(f'{numero} elevado al cuadrado es igual a {potencia}')

# Haga un algoritmo que tome el valor de un producto, le aplique el 20%
# de descuento, imprima el valor del producto inicial,
# el valor con descuento y el valor ahorrado

valor_producto = float(input('Digite el valor del producto: $'))
descuento = valor_producto * 0.20
valor_prod_final = valor_producto - descuento
print(f'El valor del producto es: {valor_producto:,}')
print(f'El descuento aplicado es de: ${descuento:,}')
print(f'EL valor final del producto es: ${valor_prod_final:,}')
