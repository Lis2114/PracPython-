
#Escribir un programa que muestre la siguiente frase 
# "Se la mejor version de ti mismo"

#forma 1: print 
print("Se la mejor version de ti mismo")

#forma 2: con una funcion pero sin arametros 
def frase(): # creamos la funcion llamamos frase
    text = "Se la mejor version de ti mismo" # asigna mensaje a variable
    return text # devuelve el text
print(frase()) # imprime el mensaje de funcion que es llamado