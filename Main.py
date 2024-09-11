from random import *
from Crud import * 
from Diseno import *
from Matrices import *
from Login import *

cantalum = random.randint(0,30 )
def main():
    usuario = {
        'root': {
            'contrasena' : 'pass',
        }
        }#usuario root para saltear el paso de crear un usuario.
    while True:
        print('1. No tienes usuario? Registrate')
        print('2. Iniciar Sesion')
        print('3. Salir')
        opcionlog = int(input('Ingrese el numero, 1-3: ' ))
        if opcionlog == 1:
            registro(usuario)
        elif opcionlog == 2:
            if inicio(usuario) == 1:
                opcion = 0
                
                matrizalumnos= crearmatriz_alumnos(cantalum)
                matrizmaterias= crearmatriz_materias()
                matriznotas= crearmatriz_notas(matrizalumnos)    
                combinado = combineta(matrizalumnos, matrizmaterias, matriznotas)
                while opcion != 8:
                    encabezados(combinado)
                    menu()
                    opcion = int(input('Ingrese la acción que desee, indicando su número: '))
                    if opcion == 1:
                        agregar_alumno(matrizalumnos)
                    elif opcion == 2:
                        leer_alumno(matrizalumnos)
                    elif opcion == 3:
                        actualizar_alumno(matrizalumnos)
                    elif opcion == 4:
                        eliminar_alumno(matrizalumnos)
                    elif opcion == 5:
                        leer_nota(matriznotas)
                    elif opcion == 6:
                        agregar_nota(matriznotas)
                    elif opcion == 7:
                        actualizar_nota(matriznotas)
                    elif opcion == 8:
                        print('Saliendo...')
                    else:
                        print('No existe una acción con el número ingresado. Por favor, ingrese del 1 al 5.')
                    #Se podria usar un try por si no se pone un numero

        elif opcionlog == 3:
            print('Saliendo....')
            break
main()