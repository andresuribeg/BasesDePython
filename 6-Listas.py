# Listas:Estructura de datos utilizada para almacenar múltiples valores en secuencia.

# Caracteristicas:

# Es una secuencia ordenada de valores
# Puede contener valores de cualquier tipo de datos
# Puede contener valores de distintos tipos de datos
# Cada posición en la lista esta asociada a un entero llamado "indice"
# Es mutable. Puede ser modificada

# Acceder a un elemento de la lista

#<Lista>[<Indice>]

letras=["a", "b","c","d"]
print(letras[0])

#Agregar elementos a una lista:

# Al final: metodo append

# <lista>.append(<elemento>)

print(letras)
letras.append("e")
print(letras)

# En un indice especifico: metodo insert

# <lista>.insert(<indice>,<elemento>)

print(letras)
letras.insert (2,"ac")
print(letras)


# Remover elementos de la lista: remove(<elemento>)

print(letras)
letras.remove("ac")
print(letras)

# NOTA: Se debe tener en cuenta que solo retira el primer valor que conicida con la busqueda
#       si existen repetidos los demás permanecerán

# Comprobar si un elemento se encuentra en la lista IN

if "c" in letras:
    letras.remove("c")
    print ("se remueve la c")
    print(letras)
else:
    print("Elemento no existe")  


# Encontrar el indice de la primer ocurrencia de un elemento en la lista
    
# <lista>.index(<elemento>)    
    
print(letras.index("d"))


# Cambiar el valor de un elemento

# <lista>[<indice>] = <nuevo_valor>

letras[2]="h"

print (letras)


# Metodos de las listas:

#<lista>.<metodo>(<parametros>)

# .count(<elemento>): Cuenta cuantas veces se repite el elemento de una lista
# .extend(<lista>): Extiende una lista agregando los elementos de otra
# .pop(): Elimina y retorna un elemento de la lista
# .reverse: Invierte el orden la lista
# .sort: Ordena la lista de forma ascedente o descendente
