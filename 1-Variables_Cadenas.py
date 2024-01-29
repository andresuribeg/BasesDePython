# Poner comentario ctrl + k + c  
# Quitar el comentario ctrl + k + u
  
# Variables:
 
# Reglas para nombrar variables:
# Los nombres de las variables deben empezar con una letra o con guion bajo.
# Los nombres de las variables no deben empezar con un número.
# Solo deben contener caracteres alfanuméricos (A-Z,a-z,0-9,_)

# <var> = <val> //Un solo igual (=) indica asignación

mi_variable=0

_mi_variable='Variable iniciada con _'
print (_mi_variable)

num_vistas=124442

# Python es case sensitive

# edad <> Edad <> EDAD

# Cadena de caracteres (String)
# Secuencia de caracteres encerrados entre comillas y usados para representar texto en el programa

cadena0='Python'
cadena1="python"

# Indexación <cadena>[<indice>]

print(cadena0[0])
print(cadena1[0])
print(cadena0[2])
# print(cadena0[6]) este sería un indice fuera de rango


# Substraer tomar una parte de una cadena <cadena>[inicio:fin] el limite no inluye el caracter final

# 0 1 2 3 4 5
# P Y T H O N

print (cadena0[1:4])  # Y T H

print (cadena0[2:])   # T H O N (toma los valores a partir del inicio)

print (cadena0[:2])   # Py (toma los valores hasta antes del final)

print (cadena0[:])   # Python (saca una copia a toda la cadena)

frase ="¡Hola, Mundo!"
print(frase[7:12])


# saltar de un caracter al siguiente

# 0 1 2 3 4 5
# P Y T H O N

# Queremos tomar los inidces 1, 3, 5

print(cadena0[1:6:2])  # Y H N

# 1 Indica donde inicia
# 6 Indica donde finaliza
# 2 Indica los saltos que debe dar entre cada caracter

# 0 1 2 3 4 5 6 7 8 9 10 11
# H O L A ,   M U N D  O  !

frase ="¡Hola, Mundo!"
print(frase[7:12:2])  # M N O


# Métodos de cadenas de caracteres

#<cadena>.<método>(<valores>)

# Capitalize(): Retorna la primer letra de una cadena en mayúscula

palabra="hola mundo"

print(palabra.capitalize())

# Otros métodos

# find
# index
#isalnum
#isalpha
#isdecimal
#isdigit
#islower
#isupper
#lower
#upper