troncales=input("Asiganturas Troncales: " )
troncales=int(troncales) #convertimos troncales en numérica
opt=input("Asiganturas Optativas: " )
opt=int(opt) #convertimos optativas en numérica
totales=troncales + opt #las sumamos y totales se convierte en númerica
totales=str(totales) #convertimos troncales en texto
troncales=str(troncales) #convertimos optativas en texto
opt=str(opt) #convertimos totales en texto
print("Tienes " + troncales + " troncales elegidas")
print("Tienes " + opt + " optativas elegidas")
print("El numero de asignaturas totales elegidas es: " + totales)
