from POO.Ciclo import Ciclo
from POO.Curso import Curso
from POO.Seccion import Seccion

class Alumno ():
    def registerData(self):
        __name=input("Ingresa tu Nombre:")
        __ciclo= Ciclo.registerCiclo('')
        __curso= Curso.registerCurso('')
        __seccion= Seccion.registerSeccion('')
        __alumn=("El alumno "+str(__name) + " esta registrado en el curso " + str(__curso)
                 + " en la Sección " + str(__seccion)+ " del "+ str(__ciclo)+"ciclo")
        return __alumn

