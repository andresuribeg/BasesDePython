# Un diccionario es una colección de pares clave-valor

#Ej: {"A": 45, "B": 30}

#características:

# Las claves del diccionario deben ser únicas e inmutables
# Los valores asociados pueden ser de cualquier tipo
# La clave se usa para acceder a su valor asociado
# Los pares clave-valor pueden ser modificados, añadidos y eliminados


# Acceder a un valor

#<diccionario>[<Clave>]

edades= {"Gino": 15, "Nora": 45}


print(edades["Nora"])

print(edades.get("Gino"))


# Añadir pares clave-valor

# <diccionario>[<clave>]=<nuevo-valor>

print (edades)

edades["Talina"] = 67

print (edades)


#  Modificar clave-valor

edades["Gino"]=20
print (edades)

# Remover clave-valor

# del <diccionario>[<clave>]

del edades["Nora"]
print (edades)

# Verificar la exitencia de un elemento en el diccionario

# <elemento> in <diccionario>

if "Gino" in edades:
    print("Gino existe")
else:
    print("Gino no existe")
