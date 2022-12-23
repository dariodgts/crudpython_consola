

# Sistema de control de usuario 
# Declaramos los arrays

Id = ['1']
Nombres =['Dario']
Contraseña =['12345']


#  Creamos el menu 

print("*****MENU DE USUARIO*****")
print("*************************")
print("1  Añadir usuario ")
print("2  Visualizar usuario ")
print("3  Borrar usuario ")
print("4  Listar ")
print("5  Salir ")
print("*************************")
type = int(input(" Seleccion: "))
while type>=1 and type<=5:
    # Si se selecciona el 1 realiza lo siguiente 
  if type==1:
    print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[")
    id = input(" Introduzca el id del usuario:")
    Nombre = input(" Introduzca el nombre del usuario: ")
    Contraseñas = input("  Introduzca la contraseña del usuario: ")
    anio= input("ingrese su año de nacimiento: ")
    ege = 2022 - int(anio)
    print("]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
    Id.append(id)
    Nombres.append(Nombre)
    Contraseña.append(Contraseñas)
    
    print(" Añadido de manera correcta ")
    # Si se selecciona el 2 realiza lo siguiente 
  elif type==2:
    id = input(" Introduzca el ID del Usuario:")
    
    if id in Id:
      index = Id.index(id)
      print("    \n\n*********DATOS DEL CLIENTE************")
      print("<----------------------------------------------->")
      print(" El id del usuario es:",Id[index])
      print(" El Nombre del usuario es:",Nombres[index])
      print(" La contraseña del usuario es:",Contraseña[index])
      print("su edad es:", ege, " años ")
      print("<------------------------------------------------>\n\n")
    else:
      print(" El usuario no fue encontrado")
# Si se selecciona el 3 realiza lo siguiente 
  elif type==3:
    id = input(" Introduzca el id del usuario:")
    if id in Id:
      index = Id.index(id)
      Id.pop(index)
      Nombres.pop(index)
      Contraseña.pop(index)
     
      print(" Eliminado correctamente ")
    else:
      print(" No se encontro el usuario")
 # Si se selecciona el 4 realiza lo siguiente 
  elif type==4:
      print("+++++++++++++++++++++++++++++++++++++++++")
      print(" Id del usuario:",Id)
      print(" Nombre del usuario:",Nombres)
      print(" Contraseña del usuario:",Contraseña)
      print("+++++++++++++++++++++++++++++++++++++++++")
 # Si se selecciona el 5 realiza lo siguiente 
  elif type==5:
    break
 
  print("******MENU DE USUARIO******")
  print("***************************")
  print("1  Añadir usuario ")
  print("2  Visualizar usuario ")
  print("3  Borrar usuario ")
  print("4  Listar ")
  print("5  Salir ")
  print("***************************")
  type = int(input(" Seleccion: "))
else:
  print(" Entrada incorrecta ") 