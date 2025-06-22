#pedir al usuario que ingrese el texto a analizar
texto = input("Ingrese un texto a eleccion:").lower()

#pedir al usuario las letras a comparar
letra1 = input("Ingrese la primera letra: ").lower()
letra2 = input("Ingrese la segunda letra: ").lower()
letra3 = input("Ingrese la tercera letra: ").lower()

#convertir las letras ingresadas en una lista
letras=[{letra1},{letra2}, {letra3}]

#contar las veces que aparece repetida cada letra
x=texto.count(letra1)
y=texto.count(letra2)
z=texto.count(letra3)

#contar cuantas palabras tiene el texto
cantidad_palabras = len(texto.split())

#letra inicial y final
texto.strip()
letra_inicial = texto[0]
letra_final = texto[-1]


#invertir el texto
invertido=texto[::-1]

#buscar la palabra python
palabra=input("palabra a buscar:")
posicion=(texto.find('palabra'))




print("------------------------------------------------")
print("CANTIDAD DE LETRAS")
print(f"Hemos encontrado la letra {letra1} repetida {x} veces")
print(f"Hemos encontrado la letra {letra2} repetida {y} veces")
print(f"Hemos encontrado la letra {letra3} repetida {z} veces")
print("________________________________________________")

print("------------------------------------------------")
print("CANTIDAD DE PALABRAS")
print(f"Hemos encontrado {cantidad_palabras} palabras en el texto")
print("------------------------------------------------")

print("------------------------------------------------")
print("LETRAS DE INICIO Y FIN")
print(f"La letra inicial {letra_inicial}  es y la final {letra_final}")
print("------------------------------------------------")

print("------------------------------------------------")
print("TEXTO INVERTIDO")
print(f"Si ordenamos tu texto al reves va a decir: {invertido}")
print("------------------------------------------------")

print("------------------------------------------------")
print("BUSCANDO LA PALABRA PYTHON")
if (posicion!=-1):
    print(f"la palabra {palabra} se encuentra en el texto")
else:
    print(f"la palabra {palabra} no se encuentra en el texto")
print("------------------------------------------------")

print("se termino")