
import random
import time
from datetime import datetime, time as datetime_time

HORARIO_INICIO = datetime_time(19, 0)  
HORARIO_FIN = datetime_time(20, 0)    
TEMPERATURA_MAXIMA = 30.0    

    
class Sensor:
    def __init__(self, tipo ):
        self._tipo = tipo  
    def obtener_lectura(self):
        pass
    
class SensorDeMovimiento(Sensor):
    def __init__(self):
        super().__init__("Movimiento" )
    def obtener_lectura(self):
        return random.choice([True, False])

class SensorDeTemperatura(Sensor):
    def __init__(self):
        super().__init__("Temperatura")
    def obtener_temperatura(self):
        return random.uniform(20.0,35.0)

class SensorDeGas(Sensor):
    def __init__(self):
        super().__init__("Gas")
    def obtener_lectura(self):
        return random.choice([True, False])
    
class Buzzer:
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

smovimiento = SensorDeMovimiento()
stemperatura = SensorDeTemperatura()
sgas = SensorDeGas()
buzzer = Buzzer()
extractor = Extractor()


# def esta_en_horario_de_trabajo():
#     ahora = datetime.now().time()
#     return HORARIO_INICIO <= ahora <= HORARIO_FIN

def activar_alarma():
    alarma_activada = False
    try:
        while True:
            if smovimiento.obtener_lectura():
                print("Movimiento detectado fuera del horario de trabajo!")
                buzzer.activar()
                alarma_activada = True
                print("Ctrl + C para desactivar")
            else:
                if not alarma_activada:
                    print("Sin movimiento")
                time.sleep(5)  # Intervalo de chequeo de 5 segundos
    except KeyboardInterrupt:
        if alarma_activada:
            buzzer.desactivar()
            alarma_activada = False
        print("Apagando alarma")
   
def desactivar_alarma():    
    buzzer.desactivar()
          

def checkear_temperatura_manual():
    temperatura = stemperatura.obtener_temperatura()
    print(f"Temperatura: {temperatura:.2f}C")
    if temperatura > TEMPERATURA_MAXIMA:
         activar=input(f"¿Activar Extractor? 1=SI / 2=NO ")
         if activar=="1":
            extractor.activar()
         elif activar=="2":
            extractor.desactivar()
        
def checkear_temperatura():
    temperatura = stemperatura.obtener_temperatura()
    print(f"Temperatura: {temperatura:.2f}C")
    if temperatura > TEMPERATURA_MAXIMA:
        extractor.activar()
    else:
        extractor.desactivar()


def checkear_fuga_de_gas():
    if sgas.obtener_lectura():
        print("Fuga de gas detectada!")
        buzzer.activar_fuga()
    else:
        buzzer.desactivar()

def activar_sirena(estado): 
    if estado==True:   
        buzzer.activar()
    else:
         buzzer.desactivar_sirena()
    

        
    