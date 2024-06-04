import random
import time
from datetime import datetime, time as datetime_time

HORARIO_INICIO = datetime_time(19, 0)
HORARIO_FIN = datetime_time(20, 0)
TEMPERATURA_MAXIMA = 30.0


class Sensor:
    def __init__(self, tipo):
        self._tipo = tipo

    def obtener_lectura(self):
        pass


class SensorDeMovimiento(Sensor):
    def __init__(self):
        super().__init__("Movimiento")

    def obtener_lectura(self):
        return random.choice([True, False])


class SensorDeTemperatura(Sensor):
    def __init__(self):
        super().__init__("Temperatura")

    def obtener_lectura(self):
        return random.uniform(20.0, 35.0)


class SensorDeGas(Sensor):
    def __init__(self):
        super().__init__("Gas")

    def obtener_lectura(self):
        return random.choice([True, False])


class Alarma:
    def activar(self):
        print("Sirena ON!")

    def desactivar(self):
        print("Sirena OFF!")


class Extractor:
    def activar(self):
        print("Activando extractor!")

    def desactivar(self):
        print("Extractor desactivado.")


class SistemaDeSeguridad:
    def __init__(self):
        self.sensores = []
        self.buzzer = Alarma()
        self.extractor = Extractor()

    def agregar_sensor(self, sensor):
        self.sensores.append(sensor)

    def activar_alarma(self):
        alarma_activada = False
        try:
            while True:
                for sensor in self.sensores:
                    if isinstance(sensor, SensorDeMovimiento) and sensor.obtener_lectura():
                        print("Movimiento detectado fuera del horario de trabajo!")
                        self.buzzer.activar()
                        alarma_activada = True
                        print("Ctrl + C para desactivar")
                    else:
                        if not alarma_activada:
                            print("Sin movimiento")
                        time.sleep(5)  # Intervalo de chequeo de 5 segundos
        except KeyboardInterrupt:
            if alarma_activada:
                self.buzzer.desactivar()
                alarma_activada = False
            print("Apagando alarma")

    def desactivar_alarma(self):
        self.buzzer.desactivar()

    def checkear_temperatura(self):
        for sensor in self.sensores:
            if isinstance(sensor, SensorDeTemperatura):
                temperatura = sensor.obtener_lectura()
                print(f"Temperatura: {temperatura:.2f}C")
                if temperatura > TEMPERATURA_MAXIMA:
                    self.extractor.activar()
                else:
                    self.extractor.desactivar()

    def checkear_temperatura_manual(self):
        for sensor in self.sensores:
            if isinstance(sensor, SensorDeTemperatura):
                temperatura = sensor.obtener_lectura()
                print(f"Temperatura: {temperatura:.2f}C")
                if temperatura > TEMPERATURA_MAXIMA:
                    activar = input(f"¿Activar Extractor? 1=SI / 2=NO ")
                    if activar == "1":
                        self.extractor.activar()
                    elif activar == "2":
                        self.extractor.desactivar()

    def checkear_fuga_de_gas(self):
        for sensor in self.sensores:
            if isinstance(sensor, SensorDeGas) and sensor.obtener_lectura():
                print("Fuga de gas detectada!")
                self.buzzer.activar()
            else:
                self.buzzer.desactivar()

    def activar_sirena(self, estado):
        if estado:
            self.buzzer.activar()
        else:
            self.buzzer.desactivar()
