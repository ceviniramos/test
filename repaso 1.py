dividendo=float (input("ingresa el dividendo: "))
while True:
    divisor = float(input("ingrese el divisor (no puede ser 0):"))

    if divisor != 0:
        break
    else:
        print ("el divisor no puede ser 0, porfavor ingrese otro numero")

resultado = dividendo/divisor 
print (f"el resulatdo de la division es:{resultado}")