import SistemaDeRotiseria
import time

# CABECERA
def cabecera_presentacion():
    print()
    print()
    print("-----------------------------------------------------------------------------------")
    print("|          ISPC Tecnicatura Superior en Innovacion con Tecnologias 4.0            |")
    print("-----------------------------------------------------------------------------------")
    print("| Materia  : Programacion                              Lenguaje : Python 2do año  |")
    print("| Profesor : Carlos Charletti                                                     |")
    print("| Repositorio:                                                                    |")
    print("|                                                                                 |")
    print("| Alumnos  :  Emiliano Arce | Palacio Braian | Mario  Pelliza | Romina Peña       |")
    print("-----------------------------------------------------------------------------------")

    time.sleep(3)


def limpia():
    from os import system
    system("cls")


cabecera_presentacion()
limpia()

sistema = SistemaDeRotiseria.SistemaDeSeguridad()
smovimiento = SistemaDeRotiseria.SensorDeMovimiento()
stemperatura = SistemaDeRotiseria.SensorDeTemperatura()
sgas = SistemaDeRotiseria.SensorDeGas()

sistema.agregar_sensor(smovimiento)
sistema.agregar_sensor(stemperatura)
sistema.agregar_sensor(sgas)

while True:
    print("""\n-1) Sistema   2) Manual   3) Salir  """)
    menu = input("""\nSeleccione una opción: """)
    if menu == "1":
        sistema.activar_alarma()

    elif menu == "2":
        menuManual = input("\n-Seleccione una opción:  1) Alarma   2) Temperatura   3) Gas   4) Sirena   ")
        if menuManual == "1":
            menuAlarma = input("""\nALARMA: 1) Activar  2) Desactivar """)
            if menuAlarma == "1":
                sistema.activar_alarma()
            elif menuAlarma == "2":
                sistema.desactivar_alarma()
        elif menuManual == "2":
            sistema.checkear_temperatura_manual()
        elif menuManual == "3":
            sistema.checkear_fuga_de_gas()
        elif menuManual == "4":
            menuSirena = input("""\nSIRENA: 1) Activar  2) Desactivar """)
            if menuSirena == "1":
                sistema.activar_sirena(True)
            elif menuSirena == "2":
                sistema.activar_sirena(False)

    elif menu == "3":
        print("\n Muchas gracias, adios.")
        exit()
    else:
        print("Opción no válida")
