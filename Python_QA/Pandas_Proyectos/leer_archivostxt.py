# pasos para abrir un archivo en python

#1. usar la funcion open() para abrir el archivo
with open("readme.txt","r") as file:
	#2. usar el metodo read() para leer el contenido del archivo
	file_stuff = file.read()

	#3. imprimir el contenido del archivo
	print(file_stuff)
print("fin de leer archivos con with open.\nahora vamos a leer linea por linea:\n")
#leer linea por linea
file = open('readme.txt','r')
line1 = file.readline()
line2= file.readline()
print(line1)
if '\n'in line2:
    print("la linea 2 tiene espacios")
 #lee todas las lineas con un ciclo

print("leyendo todas las lineas con un ciclo:")

while True:
	line = file.readline()
	if not line:
		break
	print(line)

# leer caracteres
file = open('readme.txt','r')
file.seek(2)#mueve el puntero como si fuera un cursor
characters = file.read(5)# lector de 5 caracteres
print(characters)
file.close()
#otra manera de abrir progrmas en python

