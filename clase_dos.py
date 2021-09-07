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
