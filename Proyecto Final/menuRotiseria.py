# MODULO QUE EL USUARIO VE E INTERACTUA CON EL PROGRAMA
import SistemaDeRotiseria
import time
import colorama

from colorama import init, Fore, Back, Style  


# Para que solo se de color a parte que queremos, debemos inicializar
init(autoreset=True)  # el módulo con init(autoreset=True)


# CABECERA
def cabecera_presentacion():  
    print()
    print()
    print("-----------------------------------------------------------------------------------")
    print("|          ISPC Tecnicatura Superior en Innovacion con Tecnologias 4.0            |")
    print("-----------------------------------------------------------------------------------")
    print("| Materia  : Programacion                              Lenguaje : Python 2do año  |")
    print("| Profesor : Carlos Charletti                                                     |")
    print("| Repositorio: https://github.com/braianpalacio/ISPC2                             |")
    print("|                                                                                 |")
    print("| Alumnos  :  Emiliano Arce | Palacio Braian | Mario  Pelliza                     |")
    print("|                    Guillermo Godoy | Romina Peña                                |")
    print("-----------------------------------------------------------------------------------")


    time.sleep(3)




def limpia():  # limpia la pantalla de la consola
    from os import system
    system("cls")


cabecera_presentacion()
limpia()
print("""\nBuenos días, ¿qué operacion desea realizar?""")  


while True:#MENU PARA EL USUARIO
    print(Fore.GREEN+Style.BRIGHT+"""\n1) Sistema"""+Fore.BLUE+"""   2) Manual"""+Fore.LIGHTYELLOW_EX+""" 3) Polimorfismo"""+Fore.RED+"""  4) Salir  """)
    menu = input("""\nSeleccione una opción: """).strip()
    if menu == "1":  # SISTEMA AUTOMATICO
        print(Fore.GREEN+"Para ir al menu (Ctrl + C)")
        sistema= SistemaDeRotiseria.Automatico()
        sistema.checkear()


    if menu == "2":  # MANUAL
        print(Fore.BLUE+"\n Seleccione una opción:")
        menuManual = input(Fore.BLUE+""" 1) Alarma   2) Temperatura   3) Gas  4) Cámara 5) Sirena  : """)
        if menuManual == "1":  # Alarma
            menuAlarma = input(Fore.BLUE+"""\nALARMA: 1) Activar  2) Desactivar : """)
            if menuAlarma == "1":
                SistemaDeRotiseria.activar_alarma()
            elif menuAlarma == "2":
                SistemaDeRotiseria.desactivar_alarma()
        if menuManual == "2":  # Temperatura
            SistemaDeRotiseria.checkear_temperatura_manual()
        if menuManual == "3":  # Gas
            SistemaDeRotiseria.checkear_fuga_de_gas()
        if menuManual == "4":  # Gas
            SistemaDeRotiseria.checkear_camara()
        if menuManual == "5":  # Sirena
            menuSirena = input(Fore.BLUE+"""\nSIRENA: 1) Activar  2) Desactivar  :""")
            if menuSirena == "1":
                SistemaDeRotiseria.activar_sirena(True)
            elif menuSirena == "2":
                SistemaDeRotiseria.activar_sirena(False)


    if menu == "3":  # POLIMORFISMO
        print(Fore.LIGHTYELLOW_EX+"Para ir al menu (Ctrl + C)")
        SistemaDeRotiseria.operar_administrador()
   
    elif menu == "4": # SALIR
        print(Fore.RED+"\n Muchas gracias, adios.")
        exit()
    else:
        print(Fore.RED+"Opcion no valida")
