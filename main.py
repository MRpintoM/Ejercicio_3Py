from POO.Alumno import Alumno

listAlumn=[]

op =0
def Menu():

    print("")
    print("                         Hola, Bienvenido al Menu de Opciones                    ")
    print("1. Regitro de Alumno")
    print("2. Salir")

while op!=2:
    Menu()
    op= int(input("Ingrese un Número:"))


    if (op==1):
        print("             Inscripción de Alumnos           ")
        print("             Ingresa Tus Datos.....             ")
        listAlumn.append(Alumno.registerData(''))
        for x in listAlumn:
            print(f"Hola {x}")


    elif (op==2):
        print("Salir del sistema")

else:
    print("Ingrese una opción Correcta....")



print("Hasta la próxima")



