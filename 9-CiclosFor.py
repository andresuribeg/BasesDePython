# Un ciclo es una estructura de control que permite ejecutar una 
# o varias líneas de código múltiples veces. 

# El ciclo for se usa 
# cuando sabemos la cantidad de veces que se debe repetir un grupo de instrucciones

#SINTAXIS

# for <variable> in range(<inicio>, <fin>):
    # codigo 

# <VARIABLE>:
# Puede ser utilizada en el codigo que se va a repetir
# Se actauliza automáticamente antes de cada iteración
# Debe tener un nombre descriptivo


for i in range (9): # el fin es n-1
    print(i)

# range: Funcion utilizada para obtener una secuencia de números enteros
        

#También se puede usar con 3 parámetros: range(start, stop, step)
    
    # Start: El valor inicial (0 si no se utiliza el parámetro)
    # Stop: El valor final
    # Step: El avance que tiene el ciclo (1 si no se utiliza el parámetro)

for j in range (2, 9): # el fin es n-1
    print(j)


# Ciclos sobre iterables
    
# Son estructuras que iterna sobre elementos específicos
# Cadenas de caracteres
# Listas
# Tuplas
# Diccionarios


# for <variable> in <iterable>:
    # codigo


for char in "loops":
    print (char)

for num in (1,2,3):
    print(num)    


letras={"a":1,"b": 2}    

for clave in letras:
    print(clave)

for valor in letras.values():
    print(valor)    

for clave, valor in letras.items():
    print (clave,valor)