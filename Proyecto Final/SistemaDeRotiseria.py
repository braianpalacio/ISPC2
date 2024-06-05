
import random
import time
from datetime import datetime, time as datetime_time


TEMPERATURA_MAXIMA = 30.0    

    
class Sensor:
    def __init__(self, tipo ):
        self._tipo = tipo  
    def obtener_lectura(self):
        pass
    
class SensorDeMovimiento(Sensor):# Simula la detección de movimiento. Maneja los valores aleatorios True o False
    def __init__(self):
        super().__init__("Movimiento" )
    def obtener_lectura(self):
        return random.choice([True, False, False])

class SensorDeTemperatura(Sensor):#Simula la lectura de la temperatura. Maneja valores aleatorios entre 20 y 35
    def __init__(self):
        super().__init__("Temperatura")
    def obtener_temperatura(self):
        return random.uniform(20.0,35.0)

class SensorDeGas(Sensor):#Simula la detección de gas. Maneja los valores aleatorios True o Flase
    def __init__(self):
        super().__init__("Gas")
    def obtener_lectura(self):
        return random.choice([True, False])
    
class Buzzer:#Sirena para el sensor de gas y para la alarma
    def activar(self):
        print("Sirena ON!")
    def desactivar_sirena(self):
        print("Sirena OFF!")
    def activar_fuga(self):
        print("Sirena ON!")
    def desactivar(self):
        print("Alarma desactivada.")

class Extractor:
    def activar(self):
        print("Activando extractor!")
    def desactivar(self):
        print("Extractor desactivado.")


smovimiento = SensorDeMovimiento()#Instanciamos sensores 
stemperatura = SensorDeTemperatura()
sgas = SensorDeGas()
buzzer = Buzzer()# Y actuadores
extractor = Extractor()



def activar_alarma():
    alarma_activada = False #alarma_activada para saber si esta activada
    try:#Para poder parar manualmente la alarma con Ctrl + C
        while True: #bucle inifnito hasta que se apague con las teclas Ctrl + C
            if smovimiento.obtener_lectura(): #se llama al metodo obtener_lectura del sensor de movimiento, si detecta movimiento sigue
                if not alarma_activada:# si no esta activada la alarma, se activa:
                    print("Movimiento detectado fuera del horario de trabajo!")#imprime msj
                    buzzer.activar()# activa el buzzer
                    alarma_activada = True #activa la alarma
                    print("Ctrl + C para desactivar")
            else:# si no detecta movimiento 
                if not alarma_activada: #y no esta activada la alarma
                    print("Sin movimiento")#imprime msj
                time.sleep(5)  # Espera 5 segundos
    except KeyboardInterrupt:#cuando se para el bucle
        if alarma_activada: #verifica que este activada la alarma
            buzzer.desactivar() #desactiva el buzzer
            alarma_activada = False #cambia el estado de alarma a false para apagarla
        print("Apagando alarma")#imprime msj
   
def desactivar_alarma():    
    buzzer.desactivar()
          

def checkear_temperatura_manual():#metodo para monitorizar la temperatura
    temperatura = stemperatura.obtener_temperatura()#guarda la temperatura en la variable, a traves del metodo obtener temperatura
    print(f"Temperatura: {temperatura:.2f}C") #imprime en pantalla la temperatura, el .2f es para mostrar dos digitos despues de el punto 
    if temperatura > TEMPERATURA_MAXIMA:#si la temperatura es mayor a la maxima
         activar=input(f"¿Activar Extractor? 1=SI / 2=NO ")#pregunta si quiere activar el extractor
         if activar=="1": #numero 1 para activar
            extractor.activar()
         elif activar=="2":#numero 2 para desactivar
            extractor.desactivar()
        
def checkear_temperatura():#lo mismo que el metodo anterior pero activa el extractor automaticamente
    temperatura = stemperatura.obtener_temperatura()
    print(f"Temperatura: {temperatura:.2f}C")
    if temperatura > TEMPERATURA_MAXIMA:
        extractor.activar()
    else:
        extractor.desactivar()


def checkear_fuga_de_gas():
    if sgas.obtener_lectura():#llama al metodo para saber el estado, si es verdadero 
        print("Fuga de gas detectada!")#imprime msj
        buzzer.activar_fuga()#activa buzzer
    else:#si es falso
        print("sin fuga de gas")#imprime msj
        buzzer.desactivar()#desactiva buzzer

def activar_sirena(estado): #para activar el buzzer 
    if estado==True:   
        buzzer.activar()
    else:
         buzzer.desactivar_sirena()
    

        
    