numeros = [1,2,30,4,51]
for numero in numeros:
    cuadrado = numero**2
    print (f"el cuadrado de {numero} es {cuadrado}")
print (numeros[4])

nombre = "marcos"
apellido = "MENDOZA"
frace = "Hola esta es una frace"
longitud=len(frace)
print(longitud)
print(apellido[5])
palabras = frace.split()
print (palabras)
print (palabras[0])
palabras[1] = "chau"
print(palabras) 
mayusculas = frace.upper()
print(mayusculas)
minusculas = frace.lower()
print (minusculas)
valores = [2,4,50,36]
valores.append(8)
print(valores)
del valores [2]
print (valores)

personas = {
"persona1":{
        "nombre": "Juan",
        "edad": 30,
        "ciudad": "Madrid"
},
"persona2":{
    "nombre": "Maria",
    "edad": 28,
    "ciudad": "Barcelona"
}
} 
datos=personas["persona1"]
datos2=personas["persona2"]
print (datos)
print (datos2)
print(datos2["edad"])
print(datos["ciudad"])