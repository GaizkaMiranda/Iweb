print ("Hello world")

x=5
print(x)
#float

y=5.2
print(y)

z=float(5.44)
print (z)
print(str(type(z)))

#Concatenacion
palabra1= "Hola"
palabra2= "mundo"
frase= palabra1+""+ palabra2
print(frase)

frase = "".join(palabra1,palabra2)
print(frase)

frase= "Meses:{},{} y {}".format ("Enero", "Febrero", "Marzo")
print(frase)

frase= "Meses: {1} , {0}, yy {2}"

valor1=2
valor2= 4
print (f"El resultado de multiplicar valor {valor1} y {valor2} es igual a {valor1*valor2}")


frase = "Aprendiendo"
print(frase[0])
print(frase[1])
print(frase[-1])
print(frase[-2])


mi_substring1= frase[:5]  #extrae cinco primeros caracteres
print (mi_substring1)
mi_substring2 = frase [4:]


#metodos
print(frase.count("pr"))   #cuenta veces que esta
print(frase.count("pr",0,6))
print(frase.find("pr"))  #posicion primera vez que aparece
