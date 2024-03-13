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



numero = 5
if numero > 0:
    print(str(numero) + " es mayor a 0")
    
edad = 54
altura = 175
if (edad > 14 and altura >160):
    print("Puede montarse en la montaña rusa")
else:
    print("No se puede montar en la montaña rusa")
    
numero = 5
if numero<3:
    print("El número es menor a 3")
elif (numero<6):
    print("El número está entre el 3 y el 6")
else:
    print("El número es mayor o igual a 6")
    


#while
contador=0
while(contador<5):
    contador+=1
    print("Iteración número",contador)
    
print("FIN")
    
contador=0
while (contador<5):
    contador+=1
    print("Iteración número {}".format(contador))
    if contador==3:
        break
    
print("FIN")

#FOR (FOREACH)
alumnos=["Gaizka", "Mikel", "Jon","Ruben"]
for alumno in alumnos:
    print(alumno)
    
#recorrer un string
alumno="Gaizka"
for letra in alumno:
    print(letra)
    
numeros=[5,46,3,5,2,5,55,9]
for numero in numeros:
    if numero % 2==0:
        continue
    print(numero) 

#For con else - Si termina el for completo
alumnos=["Gaizka", "Mikel", "Jon","Ruben"]
for alumno in alumnos:
    print(alumno)
else:
    print("No quedan más alumnos")

#función range() - Para hacer un bucle iterativo
for i in range(3):
    print(i)
    
for i in range(1,10,2):
    print(i)
    
alumnos=["Gaizka", "Mikel", "Jon","Ruben"]
for i in range(len(alumnos)):
    print(alumnos[i])
    
    
    
#Listas: más de un elemento de forma indexada
alumnos=["Gaizka", "Mikel", "Jon","Ruben"]
print(alumnos[0])
print(alumnos[len(alumnos)-1])
alumnos[1]="Asier"
print(alumnos[1])

alumnos.append("Manel")
print(alumnos)
alumnos.insert(0,"Markel")
print(alumnos)
alumnos.remove("Markel")
print(alumnos)
alumnos.pop()
print(alumnos)
alumno_eliminado=alumnos.pop(1)
print(alumnos)
print(alumnos.index("Gaizka"))
alumnos2= ["Jon Ander", "Andrea", "Michael"]
alumnos.extend(alumnos2)
print(alumnos)
alumnos.reverse()
print(alumnos)
sorted_alumnos= sorted(alumnos)
print(alumnos)
print(sorted_alumnos)

#Acceder a varios elementos
lista=[7,2,5,4,72,33]
print(lista[1:3])
print(lista[:3])
print(lista[2:])

#Recorrer una lista
for numero in lista:
    print(numero)
    
for i in range(len(lista)):
    print(lista[i])
    
#Tuplas - listas inmutables
valores=(1,4,2,5,13,0)
valores_mixtos=(1,4,2,5,"Trece",0)
print(valores_mixtos)
print(valores_mixtos[4:5])
    
    
    
#Mapas o diccionarios               ACCESO POR CLAVE, NO COMO EN LAS LISTAS DE FORMA INDEXADA
estudiante={
    "nombre": "Iñaki Perurena",
    "edad":30,
    "nota_media":7.25,
    "repetidor": False,
}
print(estudiante)
print(estudiante["edad"])
print(estudiante.get("edad"))
estudiante["suspensos"]=1
estudiante.update({"aprobados":5})
print(estudiante)
#Métodos de diccionarios
print(estudiante.keys())
print(estudiante.values())
print(estudiante.pop("aprobados"))
print(estudiante)
if "aprobados" in estudiante:
    print("Tiene aprobados")
else:
    print("No tiene aprobados")
    
if "Iñaki Perurena" in estudiante.values():
    print("Este es Iñaki")
else:
    print("Este no es Iñaki")
    
#Recorrer un mapa
for key in estudiante:
    print(key)

for key in estudiante:
    print(estudiante.get(key))
    
for value in estudiante.values():
    print(value)

for key,value in estudiante.items():
    print(f"El valor de {key} es {value}")
  

 
     

 #FUNCIONES
 #res ambito local, dentro de la función, y cuando se termina la ejecución no está en memoria
def suma(a,b):
    res=a+b
    print(res)
print(res)#Error
suma(1,4)
suma(a=1,b=6)

#ámbito global
a=5
def multiplica_por_dos():
    print(a*2)
multiplica_por_dos()

x = 10 
def mostrarX():
    x = x + 2 #Error, podemos acceder pero no modificar
    print("El valor de x es", x)
mostrarX()

x = 10 

def mostrarX():
    global x
    x = x + 2
    print("El valor de x es", x)  
mostrarX()


#Funciones
def saludo(nombre):
    print(f"Hola, {nombre}. !Bienvenido¡")
    
saludo("Inés")

def saludo(nombre="Anónimo"):
    print(f"Hola, {nombre}. !Bienvenido¡")
    
saludo("Inés")
saludo()

#Parámetros posicionales vs. parámetros con palabras clave (keyword arguments)
def suma(a,b):
    res=a+b
    print(res)
    
suma(1,4)
suma(a=1,b=6)

def suma(*args):#pasas una lista de valores o una tupla
    res=0
    for value in args:
        res+=value
    print(res)
suma(1,6)

def suma(**kwargs):#pasas un diccionario
    res=0
    for value in kwargs.values():
        res+=value
    print(res)
suma(a=1,b=6)



#Excepciones
try:
    divisor=int(input("Introduce un divisor: "))
    dividendo=150
    resultado= dividendo/divisor
    print(resultado)
except ValueError:
    print("Número no válido")
except ZeroDivisionError:
    print("No se puede dividir entre 0")
finally:
    print("Ejecutar finally antes de salir")
    
    
    
    
    #TypeError: unsupported operand type(s) for +: 'int' and 'str'
#print((1+'1'))

#ValueError: invalid literal for int() with base 10: 'Hola'
#print(int("Hola"))

#NameError: name 'estudiante' is not defined
#print(estudiante)

#IndexError: list index out of range
lista=[1,6,7]
#lista[5]

#KeyError: 'aprobados'
estudiante={
    "nombre": "Iñaki Perurena",
    "edad":30,
    "nota_media":7.25,
    "repetidor": False,
}
#print(estudiante["aprobados"])






