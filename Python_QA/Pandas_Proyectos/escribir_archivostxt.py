#la primera forma de abrir archivos en python es con la funcion open()
with open("escribir_archivo.txt","w") as file:
    file.write("prueba para escribir en un archivo de texto\n")
    file.write("segunda linea de prueba\n")
    print("archivo escrito con exito")
#no es necesario cerrar el archivo cuando se usa with open

#otra forma de escribir archivos en python con ciclo
Lines = ["primera linea","segunda linea","tercera linea","cuarta linea"]
with open("escribir_archivo2.txt","w") as file:
    for line in Lines:
        file.write(line + "\n")
    print("archivo escrito con exito usando ciclo")
    #no es necesario cerrar el archivo cuando se usa with open
 
    
#agregar contenido a un archivo existente
new_data = "linea agregada al final del archivo"
with open("escribir_archivo.txt","a") as file:
    file.write(new_data + "\n")
    print("contenido agregado con exito")
    #no es necesario cerrar el archivo cuando se usa with open
    
    
    #copiar contenido de un archivo a otro
with open("Readme.txt","r") as read_file:
    #abrir el archivo destino en modo escritura
    with open("escribir_archivo.txt","w") as write_file:
        #for hecho para escribir linea por linea en el nuevo archivo
        for line in read_file:
            write_file.write(line)
#no ocupamos poner close cuando usamos with open

""" ‘r’	'r'	Modo de lectura. Abre un archivo existente para lectura. Genera un error si el archivo no existe.
‘w’	'w'	Modo de escritura. Crea un nuevo archivo para escritura. Sobrescribe el archivo si ya existe.
‘a’	'a'	Modo de anexado. Abre un archivo para anexar datos. Crea el archivo si no existe.
‘x’	'x'	Modo de creación exclusiva. Crea un nuevo archivo para escritura pero genera un error si el archivo ya existe.
‘rb’	'rb'	Modo de lectura binaria. Abre un archivo binario existente para lectura.
‘wb’	'wb'	Modo de escritura binaria. Crea un nuevo archivo binario para escritura.
‘ab’	'ab'	Modo de anexado binario. Abre un archivo binario para anexar datos.
‘xb’	'xb'	Modo de creación binaria exclusiva. Crea un nuevo archivo binario para escritura pero genera un error si ya existe.
‘rt’	'rt'	Modo de lectura de texto. Abre un archivo de texto existente para lectura. (Predeterminado para archivos de texto)
‘wt’	'wt'	Modo de escritura de texto. Crea un nuevo archivo de texto para escritura. (Predeterminado para archivos de texto)
‘at’	'at'	Modo de anexado de texto. Abre un archivo de texto para anexar datos. (Predeterminado para archivos de texto)
‘xt’	'xt'	Modo de creación de texto exclusiva. Crea un nuevo archivo de texto para escritura pero genera un error si ya existe.
‘r+’	'r+'	Modo de lectura y escritura. Abre un archivo existente para lectura y escritura.
‘w+’	'w+'	Modo de escritura y lectura. Crea un nuevo archivo para lectura y escritura. Sobrescribe el archivo si ya existe.
‘a+’	'a+'	Modo de anexado y lectura. Abre un archivo para anexar y leer. Crea el archivo si no existe.
‘x+’	'x+'	Modo de creación exclusiva y lectura/escritura. Crea un nuevo archivo para lectura y escritura pero genera un error si ya existe. """