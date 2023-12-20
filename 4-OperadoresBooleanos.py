# Los operadores lógicos nos permiten trabajar con valores booleanos (True y False)

# AND: Todas las condiciones se deben cumplir para que retorne True


#        T         F
print ((5<6) and (6>8)) #False

#        F         F
print ((5>6) and (6>8)) #False

#        T         T
print ((5<6) and (6<8)) #True


# OR: SI una de las condiciones se cumple retorna True

#        T         F
print ((5<6) or (6>8)) #True

#        F         F
print ((5>6) or (6>8)) #False

# NOT: Niega el valor de una expresión

#        T              F -> T
print  ( (5<6) and not (6>8)) #True
