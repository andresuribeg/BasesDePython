#Función input(): Permite recibir datos del usuario, simepre retorna una cadena de caractéres

# Sintáxis: <var> = input(<mensaje>)

num = input("Ingrese un número: ")
print(num) #retorna la cadena

#num = input("Ingrese un número: ")
#print(num+5)  Genera error al tratar de concatenar una cadena y un entero

num = input("Ingrese un número: ")
print(num+"5") # Concatena la cadena con el 5

num = int(input("Ingrese un número: "))  # convierte la cadena a entero
print(num+5)  # hace la suma del valor de la variable + 5 y devuelve el resultado  
