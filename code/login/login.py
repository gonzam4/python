#inicio variable a 3
error=3

#creo bucle con while
while (0 < error <= 3) :
  #pido el usuario dentro del Bucle
  user=input("Usuario: ")
  # si el usuario es correcto pido password
  if user == "jorge" :
    password=input("Contraseña: ")
    #si password es correcto accedo
    if password== "1234":
      print("Bienvenidoas al programa")
      error=4
    #Este ELSE corresponde si fallo password
    else:
      print("Fallaste la contraseña")
      error=error-1
      if error== 1:
        print("Te queda "+ str(error) + " intento") 
      else:
        print("Te quedan "+ str(error) + " intentos")
    
  #Este ELSE corresponde si fallo Usuario
  else:
    print("Fallaste el usuario")
    error=error-1
    if  error== 1:
      print("Te queda "+ str(error) + " intento") 
    else:  
      print("Te quedan "+ str(error) + " intentos")   
    
  
    
    errores=10
   
