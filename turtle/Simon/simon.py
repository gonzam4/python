import turtle
import random
#Se crea pantalla
pantalla=turtle.Screen()    
pantalla.setup(800,800)   
pantalla.bgcolor('black')
turtle.setpos(0,0)

turtle.speed(500)
#para numero al azar
azar=random.randint(1, 4)
azar2=random.randint(1, 4)
azar3=random.randint(1, 4)
azar4=random.randint(1, 4)
azar5=random.randint(1, 4)
#para contador de nivel 
nivel=1
#definir azar
def azarred():
 turtle.right(180)
 turtle.color("red")
 relleno(-7,207)
 turtle.right(90)
 norelleno(-10,204)
 turtle.left(180)
def azargreen():
  turtle.left(90)
  turtle.color("green")
  relleno(100,107)
  turtle.right(90)
  norelleno(97,110)
  turtle.right(90)
def azaryellow():
  turtle.color("yellow")
  relleno(0,0)
  turtle.right(90)
  norelleno(3,3)
def azarblue():
  turtle.right(90)
  turtle.color("blue")
  relleno(-107,100)
  turtle.right(90)
  norelleno(-104,97)
  turtle.left(90)

#Puntero y tablero
turtle.pensize("3")
#iluminarse y dejar de hacerlo para indicar color
def relleno(m,n):
  turtle.speed(100)
  turtle.setpos(m,n)
  turtle.speed(10)
  turtle.begin_fill()
  tablero(m,n)
  turtle.end_fill()
def norelleno(a,b):
 turtle.speed(1000)
 turtle.color("black")
 turtle.setpos(a,b)
 turtle.pendown()
 turtle.begin_fill()
 turtle.circle(97,90)
 turtle.penup()
 turtle.setpos(a,b)
 turtle.pendown()
 turtle.forward(47)
 turtle.right(90)
 turtle.circle(47,90)
 turtle.right(90)
 turtle.forward(47)
 turtle.penup()
 turtle.end_fill()

 
#dibujar el tablero
def tablero(x,y):
 turtle.setpos(x,y)
 turtle.pendown()
 turtle.circle(100,90)
 turtle.penup()
 turtle.setpos(x,y)
 turtle.pendown()
 turtle.forward(50)
 turtle.right(90)
 turtle.circle(50,90)
 turtle.right(90)
 turtle.forward(50)
 turtle.penup()
 turtle.left(90)

def dibujo():
  turtle.color("yellow")
  tablero(0,0)
  turtle.color("green")
  tablero(100,107)
  turtle.color("red")
  tablero(-7,207)
  turtle.color("blue")
  tablero(-107,100)
  turtle.setpos(-40,115)
  turtle.color("white")
  turtle.write(("Simon" ), font=("Times New Roman", 20))
  turtle.setpos(-35,85)
  turtle.write(("dice..." ), font=("Times New Roman", 20))
  turtle.setpos(-125,150)
  turtle.write(("1" ), font=("Times New Roman", 20))
  turtle.setpos(105,150)
  turtle.write(("2" ), font=("Times New Roman", 20))
  turtle.setpos(105,40)
  turtle.write(("3" ), font=("Times New Roman", 20))
  turtle.setpos(-125,40)
  turtle.write(("4" ), font=("Times New Roman", 20))
  turtle.penup()
  turtle.hideturtle()
  
  
#siguiente nivel
azar6=random.randint(1,6)
azar7=random.randint(1,6)
azar8=random.randint(1,6)
azar9=random.randint(1,6)
azar10=random.randint(1,6)
azar11=random.randint(1,6)

def tablero2(x,y):
 turtle.setpos(x,y)
 turtle.pendown()
 turtle.circle(100,60)
 turtle.penup()
 turtle.setpos(x,y)
 turtle.pendown()
 turtle.forward(25)
 turtle.right(60)
 turtle.circle(50,60)
 turtle.right(60)
 turtle.forward(25)
 turtle.penup()
 turtle.left(60)
 
def dibujo2():
  turtle.color("yellow")
  tablero2(0,0)
  turtle.color("green")
  tablero2(85,50)
  turtle.color("red")
  tablero2(85,150)
  turtle.color("blue")
  tablero2(-5,200)
  turtle.color("orange")
  tablero2(-85,150)
  turtle.color("purple")
  tablero2(-85,50)
  turtle.setpos(-35,105)
  turtle.color("white")
  turtle.write(("Simon" ), font=("Times New Roman", 20))
  turtle.setpos(-30,75)
  turtle.write(("dice..." ), font=("Times New Roman", 20))
  turtle.setpos(85,0)
  turtle.write(("1" ), font=("Times New Roman", 20))
  turtle.setpos(110,95)
  turtle.write(("2" ), font=("Times New Roman", 20))
  turtle.setpos(65,190)
  turtle.write(("3" ), font=("Times New Roman", 20))
  turtle.setpos(-70,190)
  turtle.write(("4" ), font=("Times New Roman", 20))
  turtle.setpos(-120,95)
  turtle.write(("5" ), font=("Times New Roman", 20))
  turtle.setpos(-85,0)
  turtle.write(("6" ), font=("Times New Roman", 20))
  turtle.penup()
  turtle.hideturtle()
  
  
def relleno2(m,n):
  turtle.speed(100)
  turtle.setpos(m,n)
  turtle.speed(10)
  turtle.begin_fill()
  tablero2(m,n)
  turtle.end_fill()
def norelleno2(a,b):
 turtle.speed(500)
 turtle.color("black")
 turtle.setpos(a,b)
 turtle.pendown()
 turtle.begin_fill()
 turtle.circle(97,60)
 turtle.penup()
 turtle.setpos(a,b)
 turtle.pendown()
 turtle.forward(22)
 turtle.right(60)
 turtle.circle(47,60)
 turtle.right(60)
 turtle.forward(22)
 turtle.penup()
 turtle.end_fill()
  
def azarred2():
 turtle.left(120)
 turtle.color("red")
 relleno2(85,150)
 turtle.right(60)
 norelleno2(82,153)
 turtle.left(240)
def azargreen2():
  turtle.left(60)
  turtle.color("green")
  relleno2(85,50)
  turtle.right(60)
  norelleno2(85,53)
  turtle.right(60)
def azaryellow2():
  turtle.color("yellow")
  relleno2(0,0)
  turtle.right(60)
  norelleno2(3,3)
def azarblue2():
  turtle.left(180)
  turtle.color("blue")
  relleno2(-5,200)
  turtle.right(60)
  norelleno2(-8,197)
  turtle.left(180)
def azarpurple():
  turtle.right(60)
  turtle.color("purple")
  relleno2(-85,50)
  turtle.right(60)
  norelleno2(-80,47)
  turtle.left(60)
def azarorange():
  turtle.right(120)
  turtle.color("orange")
  relleno2(-85,150)
  turtle.right(60)
  norelleno2(-85,147)
  turtle.left(120)
  
  
  
  
  
  
  
  
  

#comienza el juego
usuario = input("Escribe tu nombre de usuario:")
empezar=input( usuario + " te gustaria jugar a Simon dice...?:")
if (empezar=="si") or (empezar=="Si"):
  print("Intenta seguir la secuencia de colores. Recuerda, para seleccionar rojo pulsa 1, para seleccionar verde 2, amarillo 3 y azul 4. ")
while (empezar=="Si") or (empezar=="si"):
 dibujo()
 nivel1=input("Preparado para comenzar el nivel?:")
 if (nivel1=="Si") or (nivel1=="si"):
  while (nivel<6):
   if (nivel==1):
    if azar==1:
     azarred()
    if azar==2:
     azargreen()
    if azar==3:
     azaryellow()
    if azar==4:
     azarblue()
    print ("Ahora te toca seguir el patron")
    primero=input ("Que color ha elegido?:")
    if int(primero)==azar:
     print ("Correcto, el juego continua...")
     nivel=nivel+1
    else:
     print("Lo siento, el numero correcto era " + str(azar) + ". Has perdido.")
     volver=input("Deseas volver a jugar?:")
     if (volver=="si") or (volver=="Si"):
      nivel=1
     else:
      empezar="no"
      nivel=20
     
     
     
     
     
   if (nivel==2):
    if azar==1:
     azarred()
    if azar==2:
     azargreen()
    if azar==3:
     azaryellow()
    if azar==4:
     azarblue()
    
    if azar2==1:
     azarred()
    if azar2==2:
     azargreen()
    if azar2==3:
     azaryellow()
    if azar2==4:
     azarblue()
    print ("Ahora te toca seguir el patron")
    primero=input ("Que color ha elegido?:")
    segundo=input ("Cual ha sido el segundo color?:")
    if (int(primero)==azar) and (int(segundo)==azar2):
     print ("Correcto, el juego continua...")
     nivel=nivel+1
    else:
     print("Lo siento, la secuencia correcta era " + str(azar) + ", " + str(azar2) + ". Has perdido.")
     volver=input("Deseas volver a jugar?:")
     if (volver=="si") or (volver=="Si"):
      nivel=1
     else:
      empezar="no"     
      nivel=20
     
     
     
     
      
     
   if (nivel==3):
    if azar==1:
     azarred()
    if azar==2:
     azargreen()
    if azar==3:
     azaryellow()
    if azar==4:
     azarblue()
    
    if azar2==1:
     azarred()
    if azar2==2:
     azargreen()
    if azar2==3:
     azaryellow()
    if azar2==4:
     azarblue()

    if azar3==1:
     azarred()
    if azar3==2:
     azargreen()
    if azar3==3:
     azaryellow()
    if azar3==4:
     azarblue()
    print ("Ahora te toca seguir el patron")
    primero=input ("Que color ha elegido?:")
    segundo=input ("Cual ha sido el segundo color?:")
    tercero=input ("Cual ha sido el tercer color?:")   
    if (int(primero)==azar) and (int(segundo)==azar2) and (int(tercero)==azar3):
     print ("Correcto, el juego continua...")
     nivel=nivel+1
    else:
     print("Lo siento, la secuencia correcta era " + str(azar) + ", " + str(azar2) + ", " + str(azar3) + ". Has perdido.")
     volver=input("Deseas volver a jugar?:")
     if (volver=="si") or (volver=="Si"):
      nivel=1
     else:
      empezar="no"   
      nivel=20
     
     
     
     
    
   if (nivel==4):
    if azar==1:
     azarred()
    if azar==2:
     azargreen()
    if azar==3:
     azaryellow()
    if azar==4:
     azarblue()
     
    if azar2==1:
     azarred()
    if azar2==2:
     azargreen()
    if azar2==3:
     azaryellow()
    if azar2==4:
     azarblue()
 
    if azar3==1:
     azarred()
    if azar3==2:
     azargreen()
    if azar3==3:
     azaryellow()
    if azar3==4:
     azarblue()
    
    if azar4==1:
     azarred()
    if azar4==2:
     azargreen()
    if azar4==3:
     azaryellow()
    if azar4==4:
     azarblue()
    print ("Ahora te toca seguir el patron")
    primero=input ("Que color ha elegido?:")
    segundo=input ("Cual ha sido el segundo color?:")
    tercero=input ("Cual ha sido el tercer color?:") 
    cuarto=input ("Cual ha sido el cuarto color?:")
    if (int(primero)==azar) and (int(segundo)==azar2) and (int(tercero)==azar3) and (int(cuarto)==azar4):
     print ("Correcto, el juego continua...")
     nivel=nivel+1
    else:
     print("Lo siento, la secuencia correcta era " + str(azar) + ", " + str(azar2) + ", " + str(azar3) + ", " + str(azar4) + ". Has perdido.")
     volver=input("Deseas volver a jugar?:")
     if (volver=="si") or (volver=="Si"):
      nivel=1
     else:
      empezar="no"    
      nivel=20
      
     
     
    
   if (nivel==5):
    if azar==1:
     azarred()
    if azar==2:
     azargreen()
    if azar==3:
     azaryellow()
    if azar==4:
     azarblue()
     
    if azar2==1:
     azarred()
    if azar2==2:
     azargreen()
    if azar2==3:
     azaryellow()
    if azar2==4:
     azarblue()  

    if azar3==1: 
     azarred()
    if azar3==2:
     azargreen()
    if azar3==3:
     azaryellow()
    if azar3==4:
     azarblue()
     
    if azar4==1:
     azarred()
    if azar4==2:
     azargreen()
    if azar4==3:
     azaryellow()
    if azar4==4:
     azarblue()
   
    if azar5==1:
     azarred()
    if azar5==2:
     azargreen()
    if azar5==3:
     azaryellow()
    if azar5==4:
     azarblue()
    print ("Ahora te toca seguir el patron")
    primero=input ("Que color ha elegido?:")
    segundo=input ("Cual ha sido el segundo color?:")
    tercero=input ("Cual ha sido el tercer color?:") 
    cuarto=input ("Cual ha sido el cuarto color?:")
    quinto=input ("Cual ha sido el quinto color?:")
    if (int(primero)==azar) and (int(segundo)==azar2) and (int(tercero)==azar3) and (int(cuarto)==azar4) and (int(quinto)==azar5):
     print ("Has ganado!")
     empezar="no"
     nivel=nivel+1
    else:
     print("Lo siento, la secuencia correcta era " + str(azar) + ", " + str(azar2) + ", " + str(azar3) + ", " + str(azar4) + ", " + str(azar5) + ". Has perdido.")
     volver=input("Deseas volver a jugar?:")
     if (volver=="si") or (volver=="Si"):
      nivel=1
     else:
      empezar="no"   
      nivel=20

 else:
   listo=input("Cuando estes listo escribe la palabra YA:")
   if (listo=="ya") or (listo=="Ya") or (listo=="YA"):
    nivel1="si" 
   
   
   
   
   
   
#nuevonivel
 while (nivel>5) and (nivel<12):
  desafio=input("Te gustaria hacer el proximo desafio de Simon dice?:")
  if (desafio=="si") or (desafio=="Si"):
   turtle.color("black")
   turtle.setpos(-150,0)
   turtle.begin_fill()
   for i in range (4):
    turtle.forward(300)
    turtle.left(90)
   turtle.end_fill()
   dibujo2()
   if (nivel==6):
     if azar6==1:
      azaryellow2()
     if azar6==2:
      azargreen2()
     if azar6==3:
      azarred2()
     if azar6==4:
      azarblue2()
     if azar6==5:
      azarorange()
     if azar6==6:
      azarpurple()
     print ("Ahora te toca seguir el patron")
     sexto=input ("Que color ha elegido?:")
     if int(sexto)==azar6:
      print ("Correcto, el juego continua...")
      nivel=nivel+1
     else:
      print("Lo siento, el numero correcto era " + str(azar6))
      volver=input("Deseas volver a jugar?:")
      if (volver=="si") or (volver=="Si"):
       nivel=1
      else:
       empezar="no"
       nivel=20
     
     
     
     
     
     
   if (nivel==7):
     if azar6==1:
      azaryellow2()
     if azar6==2:
      azargreen2()
     if azar6==3:
      azarred2()
     if azar6==4:
      azarblue2()
     if azar6==5:
      azarorange()
     if azar6==6:
      azarpurple()
    
     if azar7==1:
      azaryellow2()
     if azar7==2:
      azargreen2()
     if azar7==3:
      azarred2()
     if azar7==4:
      azarblue2()
     if azar7==5:
      azarorange()
     if azar7==6:
      azarpurple()


     print ("Ahora te toca seguir el patron")
     sexto=input ("Que color ha elegido?:")
     septimo=input ("Cual ha sido el segundo color?:")
     if (int(sexto)==azar6) and (int(septimo)==azar7):
      print ("Correcto, el juego continua...")
      nivel=nivel+1
     else:
      print("Lo siento, la secuencia correcta era " + str(azar6) + ", " + str(azar7)+ ". Has perdido.")
      volver=input("Deseas volver a jugar?:")
      if (volver=="si") or (volver=="Si"):
       nivel=1
      else:
       empezar="no"   
       nivel=20
     
     
     
     
     
     
   if (nivel==8):
     if azar6==1:
      azaryellow2()
     if azar6==2:
      azargreen2()
     if azar6==3:
      azarred2()
     if azar6==4:
      azarblue2()
     if azar6==5:
      azarorange()
     if azar6==6:
      azarpurple()
    
     if azar7==1:
      azaryellow2()
     if azar7==2:
      azargreen2()
     if azar7==3:
      azarred2()
     if azar7==4:
      azarblue2()
     if azar7==5:
      azarorange()
     if azar7==6:
      azarpurple()
    
     if azar8==1:
      azaryellow2()
     if azar8==2:
      azargreen2()
     if azar8==3:
      azarred2()
     if azar8==4:
      azarblue2()
     if azar8==5:
      azarorange()
     if azar8==6:
      azarpurple()
    
   
   
     print ("Ahora te toca seguir el patron")
     sexto=input ("Que color ha elegido?:")
     septimo=input ("Cual ha sido el segundo color?:")
     octavo=input ("Cual ha sido el tercer color?:")   
     if (int(sexto)==azar6) and (int(septimo)==azar7) and (int(octavo)==azar8):
      print ("Correcto, el juego continua...")
      nivel=nivel+1
     else:
      print("Lo siento, la secuencia correcta era " + str(azar6) + ", " + str(azar7) + ", " + str(azar8) + ". Has perdido.")
      volver=input("Deseas volver a jugar?:")
      if (volver=="si") or (volver=="Si"):
       nivel=1
      else:
       empezar="no"   
       nivel=20
     
     
     
     
    
   if (nivel==9):
     if azar6==1:
      azaryellow2()
     if azar6==2:
      azargreen2()
     if azar6==3:
      azarred2()
     if azar6==4:
      azarblue2()
     if azar6==5:
      azarorange()
     if azar6==6:
      azarpurple()
    
     if azar7==1:
      azaryellow2()
     if azar7==2:
      azargreen2()
     if azar7==3:
      azarred2()
     if azar7==4:
      azarblue2()
     if azar7==5:
      azarorange()
     if azar7==6:
      azarpurple()
    
     if azar8==1:
      azaryellow2()
     if azar8==2:
      azargreen2()
     if azar8==3:
      azarred2()
     if azar8==4:
      azarblue2()
     if azar8==5:
      azarorange()
     if azar8==6:
      azarpurple()
    
     if azar9==1:
      azaryellow2()
     if azar9==2:
      azargreen2()
     if azar9==3:
      azarred2()
     if azar9==4:
      azarblue2()
     if azar9==5:
      azarorange()
     if azar9==6:
      azarpurple()
   
   
     print ("Ahora te toca seguir el patron")
     sexto=input ("Que color ha elegido?:")
     septimo=input ("Cual ha sido el segundo color?:")
     octavo=input ("Cual ha sido el tercer color?:")   
     noveno=input("Cual ha sido el cuarto color?:")
     if (int(sexto)==azar6) and (int(septimo)==azar7) and (int(octavo)==azar8) and (int(noveno)==azar9):
      print ("Correcto, el juego continua...")
      nivel=nivel+1    
     else:
      print("Lo siento, la secuencia correcta era " + str(azar6) + ", " + str(azar7) + ", " + str(azar8) + ", " + str(azar9) + ". Has perdido.")
      volver=input("Deseas volver a jugar?:")
      if (volver=="si") or (volver=="Si"):
       nivel=1
      else:
       empezar="no"    
       nivel=20
     
     
     
     
     
          
    
   if (nivel==10):
     if azar6==1:
      azaryellow2()
     if azar6==2:
      azargreen2()
     if azar6==3:
      azarred2()
     if azar6==4:
      azarblue2()
     if azar6==5:
      azarorange()
     if azar6==6:
      azarpurple()
    
     if azar7==1:
      azaryellow2()
     if azar7==2:
      azargreen2()
     if azar7==3:
      azarred2()
     if azar7==4:
      azarblue2()
     if azar7==5:
      azarorange()
     if azar7==6:
      azarpurple()
    
     if azar8==1:
      azaryellow2()
     if azar8==2:
      azargreen2()
     if azar8==3:
      azarred2()
     if azar8==4:
      azarblue2()
     if azar8==5:
      azarorange()
     if azar8==6:
      azarpurple()
    
     if azar9==1:
      azaryellow2()
     if azar9==2:
      azargreen2()
     if azar9==3:
      azarred2()
     if azar9==4:
      azarblue2()
     if azar9==5:
      azarorange()
     if azar9==6:
      azarpurple()
      
     if azar10==1:
      azaryellow2()
     if azar10==2:
      azargreen2()
     if azar10==3:
      azarred2()
     if azar10==4:
      azarblue2()
     if azar10==5:
      azarorange()
     if azar10==6:
      azarpurple()
   
   
     print ("Ahora te toca seguir el patron")
     sexto=input ("Que color ha elegido?:")
     septimo=input ("Cual ha sido el segundo color?:")
     octavo=input ("Cual ha sido el tercer color?:")   
     noveno=input("Cual ha sido el cuarto color?:")
     decimo=input("Cual ha sido el quinto color?:")
     if (int(sexto)==azar6) and (int(septimo)==azar7) and (int(octavo)==azar8) and (int(noveno)==azar9) and (int(decimo)==azar10):
      print ("Correcto, el juego continua...")
      nivel=nivel+1    
     else:
      print("Lo siento, la secuencia correcta era " + str(azar6) + ", " + str(azar7) + ", " + str(azar8) + ", " + str(azar9) + ", " + str(azar10) + ". Has perdido.")
      volver=input("Deseas volver a jugar?:")
      if (volver=="si") or (volver=="Si"):
       nivel=1
      else:
       empezar=="no"  
       nivel=20
     
   if (nivel==11):
     if azar6==1:
      azaryellow2()
     if azar6==2:
      azargreen2()
     if azar6==3:
      azarred2()
     if azar6==4:
      azarblue2()
     if azar6==5:
      azarorange()
     if azar6==6:
      azarpurple()
    
     if azar7==1:
      azaryellow2()
     if azar7==2:
      azargreen2()
     if azar7==3:
      azarred2()
     if azar7==4:
      azarblue2()
     if azar7==5:
      azarorange()
     if azar7==6:
      azarpurple()
    
     if azar8==1:
      azaryellow2()
     if azar8==2:
      azargreen2()
     if azar8==3:
      azarred2()
     if azar8==4:
      azarblue2()
     if azar8==5:
      azarorange()
     if azar8==6:
      azarpurple()
    
     if azar9==1:
      azaryellow2()
     if azar9==2:
      azargreen2()
     if azar9==3:
      azarred2()
     if azar9==4:
      azarblue2()
     if azar9==5:
      azarorange()
     if azar9==6:
      azarpurple()
      
     if azar10==1:
      azaryellow2()
     if azar10==2:
      azargreen2()
     if azar10==3:
      azarred2()
     if azar10==4:
      azarblue2()
     if azar10==5:
      azarorange()
     if azar10==6:
      azarpurple()
      
     if azar11==1:
      azaryellow2()
     if azar11==2:
      azargreen2()
     if azar11==3:
      azarred2()
     if azar11==4:
      azarblue2()
     if azar11==5:
      azarorange()
     if azar11==6:
      azarpurple()
   
   
     print ("Ahora te toca seguir el patron")
     sexto=input ("Que color ha elegido?:")
     septimo=input ("Cual ha sido el segundo color?:")
     octavo=input ("Cual ha sido el tercer color?:")   
     noveno=input("Cual ha sido el cuarto color?:")
     decimo=input("Cual ha sido el quinto color?:")
     onceavo=input("Cual ha sido el sexto color?:")
     if (int(sexto)==azar6) and (int(septimo)==azar7) and (int(octavo)==azar8) and (int(noveno)==azar9) and (int(decimo)==azar10) and (int(onceavo)==azar11):
      turtle.setpos(-150,215)
      turtle.begin_fill()
      for i in range (4):
       turtle.color("black")
       turtle.forward(300)
       turtle.right(90)
      turtle.end_fill()
      turtle.setpos(-150,105)
      turtle.color("aquamarine")
      turtle.write(("Has completado todos los niveles!" ), font=("Times New Roman", 20))
      turtle.setpos(-80,70)
      turtle.write(("ENHORABUENA!" ), font=("Times New Roman", 20))
      print("ENHORABUENA")
      nivel=20  
     else:
      print("Lo siento, la secuencia correcta era " + str(azar6) + ", " + str(azar7) + ", " + str(azar8) + ", " + str(azar9) + ", " + str(azar10) + ", " + str(azar11) + ". Has perdido.")
      volver=input("Deseas volver a jugar?:")
      if (volver=="si") or (volver=="Si"):
       nivel=1
      else:
       empezar="no"     
       nivel=20
     
  
  else:
    print("Esperamos volver a jugar contigo, " + usuario)
    empezar="no" 
    nivel=20



if (empezar!="si") or (empezar!="Si"):
 print("Hasta la proxima.")
