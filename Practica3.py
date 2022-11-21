nombre=input ("Ingrese su Nombre: "+"\n")
#buscar_subcadena=nombre.find("a" or "b")
primera_letra = nombre[:1]
if (primera_letra== "a" or primera_letra=="b" or primera_letra=="c" or primera_letra=="d" or primera_letra=="e" or primera_letra=="f" or primera_letra=="g" or primera_letra=="h" or primera_letra=="i" or primera_letra=="j" or primera_letra=="k" or primera_letra=="l" or primera_letra=="m"):
   curso= input("Por Favor ingrese su Turno: "+"\n") 
   print ("Usted corresponde al: ", end="")
   if (curso== "tarde"):
    print ("Grupo  A")
   else:
    print ("Grupo B") 
else:
    curso= input("Por Favor ngrese su turno!: "+"\n") 
    print ("Usted actualmente corresponde al: ", end="")
    if (curso== "noche"):
     print ("Grupo A")
    else:
     print ("Grupo B") 

