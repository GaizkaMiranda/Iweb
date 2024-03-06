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
print(frase.count("pr",0,6)) #cuenta cuántas veces aparece una subcadena específica dentro de otra cadena
print(frase.find("pr"))  #posicion primera vez que aparece


#operadores de comparación
print (x>y)
print (y<9)
print (x>y and x>10)



edad= 54
altura = 175
if (edad>14 and altura> 160):
    print ("Se puede montar en la montaña rusa")
else: ("no se puede montar")

numero = 5
if numero < 3:
    print ("El numero es menor a 3")
elif (numero <6)
print ("numeoo o entre 3 y 6")


#while
contador=0
while (contador <5):
    contador+=1
    print ("Iteracion, numero" , contador)
    
    print("FIN")
 
 
 contador=0   
 while (contador <5):
      contador+=1
      print ("Iteracion, numero {}" . format (contador))
if contador ==3
break



#FOR
alumnos = ["gaizka", "mikel", "jon"]
for alumno in alumnos:
    print (alumno)
    
    
    #recorrer un String
    alumno= "gaizka"
    for letra in alumno:
        print(letra)
        

 #for con else- si termina el for completo
 alumnos = ["gaizka", "mikel", "jon"]
 for alumno in alumnos:
     print(alumno)
 else: print("No quedan mas alumnos")
 
 
 #funcion range()- bucle iterativo
 for i in range (1,10,20):
     print(i)
     
for i in range(3):
    print(i)


#Listas: mas de un elemento de forma indexada
alumnos = ["gaizka", "mikel", "jon"]


 
     

 