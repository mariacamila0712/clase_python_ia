# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 19:24:31 2021

@author: Maria Camila
"""

# Tipos de colecciones

# Listas o vectores
# Tipos de datos mutables y ordenado

a = []
a = [2, 3, 4]
b = [2, True, 'Hola', 3.4]
c = [2, [3, 4], ['Hola', 'Mundo'], [2.3, [2.4, 2.5], 2.6]]

for valor in a:
    print(valor)

for valor in b:
    print(valor)

for valor in c:
    print(valor)

a[0] = 7
print(b[2])
print(c[2][1])
print(c[3][1][1])

a.append(5)  # Agrega el elemento al final de la lista
a.remove(3)  # Elimina el elemento que coincida con el valor
a.pop()  # Elimina el ultimo elemento del vector
# a.pop(2)  # Elimina un elemento por posicion
a.clear()  # Elimina todos los elementos del vector
# del a
4 in a  # Busca el elemento 4 dentro de a
len(a)  # Cantidad de elementos del vector
a = b  # Asignacion de b en el mismo espacio de memoria de a
id(a)  # Convierte a decimal la direccion en memoria de un objeto
a = b.copy()  # Copia los elementos de b en a
b = a[:3]  # Cuando se quiere escoger desde 0 se puede omitir el 1er numero
b = a[2:]  # Traer los elementos hasta el final
b = a[:]  # Trae todo

# Tuplas
# Tipos de datos inmutable y ordenado
a = (1, 2, 3, 4)
a = ()
print(a[1])
a = (2, 3, 4)
b = (2, True, 'Hola', 3.4)
c = (2, [3, 4], ['Hola', 'Mundo'], [2.3, [2.4, 2.5], 2.6])
4 in a


# Set
# Mutable pero no ordenado
# No permiten arrays en su interior
a = {1, 2, 3, 4}
a = set()
b = {2, True, 'Hola', 3.4}

# Diccionarios
# Mutables y no ordenados
a = {}
a = {'nombre': 'Maria', 'apellido': 'Maza'}
a = {1: 'Maria', 2: 'Maza'}

for valor in a:
    print(valor)

for valor in a.values():
    print(valor)

for valor in a.keys():
    print(valor)

for valor in a.items():
    print(valor)

for llave, valor in a.items():
    print(f'Llave: {llave}, Valor: {valor}')


# Funciones

def nombre_funcion():
    pass


def saludar():
    print('Hola Mundo')


def saludar(nombre):
    print(f'Hola {nombre}')


# Python no permite la Sobrecarga de métodos
# Parametros opcionales

def saludar(nombre= 'Mundo'):
    print(f'Hola {nombre}')


def saludar(nombre, apellido=""):
    print(f'Hola {nombre} {apellido}')


def saludar(nombre="Mundo", apellido=""):
    print(f'Hola {nombre} {apellido}')


# No se puede tener un párametro obligatorio despues de un parámetro opcional
# def saludar(nombre, apellido="", segundo_apellido):
    print(f'Hola {nombre} {apellido}')

# Parámetros ilimitados

def saludar(*nombres):
    for nombre in nombres:
        print(f'Hola {nombre}')


def saludar(*nombres, apellido = ""):
    for nombre in nombres:
        print(f'Hola {nombre}')
    print(f'Apellido {apellido}')


def saludar(*nombres, apellido):
    for nombre in nombres:
        print(f'Hola {nombre}')
    print(f'Apellido {apellido}')

def saludar(**nombres):
    print(nombres)


def resta(a, b):
    print(a - b)

def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicación = a * b
    división = a / b
    return suma, resta, multiplicación, división

resultados = operaciones(4, 5)

suma, res, mult, div = operaciones(4, 5)

suma, _, _, div = operaciones(4, 5)