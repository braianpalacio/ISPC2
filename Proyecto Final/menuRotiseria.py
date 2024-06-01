# MODULO QUE EL USUARIO VE E INTERACTUA CON EL PROGRAMA
import SistemaDeRotiseria
import time
from colorama import init, Fore, Back, Style  # Para dar color a la consola

# Para que solo se de color a parte que queremos, debemos inicializar
init(autoreset=True)  # el módulo con init(autoreset=True)

# CABECERA
def cabecera_presentacion():  # parte grafica para consola
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


def limpia():  # limpia la pantalla de la consola
    from os import system
    system("cls")

cabecera_presentacion()
limpia()


while True:#MENU PARA EL USUARIO
    print("""\n-1) Sistema   2) Manual   3) Salir  """)
    menu = input("""\nSeleccione una opción: """)
    # if menu == "1":#SISTEMA AUTOMATICO
    # sistema ()

    if menu == "2":  # MANUAL
        menuManual = input(
            "\n-Seleccione una opción:  1) Alarma   2) Temperatura   3) Gas   4) Sirena   ")
        if menuManual == "1":  # Alarma
            menuAlarma = input("""\nALARMA: 1) Activar  2) Desactivar """)
            if menuAlarma == "1":
                SistemaDeRotiseria.activar_alarma()
            elif menuAlarma == "2":
                SistemaDeRotiseria.desactivar_alarma()
        if menuManual == "2":  # Temperatura
            SistemaDeRotiseria.checkear_temperatura_manual()
        if menuManual == "3":  # Gas
            SistemaDeRotiseria.checkear_fuga_de_gas()
        if menuManual == "4":  # Sirena
            menuSirena = input("""\nSIRENA: 1) Activar  2) Desactivar """)
            if menuSirena == "1":
                SistemaDeRotiseria.activar_sirena(True)
            elif menuSirena == "2":
                SistemaDeRotiseria.activar_sirena(False)

    elif menu == "3":
        print("\n Muchas gracias, adios.")
        exit()
    else:
        print(+"Opcion no valida")
