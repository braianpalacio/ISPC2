import time
import random
from random import choice




class RotiseriaIoT():
    def __init__(self, tipo):
        self.tipo = tipo
    def operar(self):
        pass
    def obtener_lectura(self):
        pass




class SensorTemperatura(RotiseriaIoT):
    def __init__(self):
        super().__init__("temperatura")
 
    def obtener_lectura(self):
        self.temperatura = round(random.uniform(-10, 40))
        return self.temperatura


    def operar(self):
        temperatura = self.obtener_lectura
        return f"Temperatura detectada: {temperatura} grados."




class SensorGas(RotiseriaIoT):
    def __init__(self):
        super().__init__("gas")


    def obtener_lectura(self):
        return round(random.uniform(300, 10000))


    def operar(self):
        gas = self.obtener_lectura
        return f"Nivel de gas: {gas} ppm."




class SensorMovimiento(RotiseriaIoT):
    def __init__(self):
        super().__init__("movimiento")




    def obtener_lectura(self):
        return random.choice(["Si", "No"])


    def operar(self):
        movimiento = self.obtener_lectura
        return f"Movimiento detectado: {movimiento} ."


class CamaraSeguridad(RotiseriaIoT):
    def __init__(self):
        super().__init__("camara")




    def obtener_lectura(self):
        return random.choice(["Si", "No"])


    def operar(self):
        movimiento = self.obtener_lectura
        return f"Cámara funcionando: {camara} ."

class AdministradorSensores:
    def __init__(self):
        self.sensores = []


    def agregar_sensor(self, sensor):
        self.sensores.append(sensor)


    def operar(self):
        datos = {}
        for sensor in self.sensores:
            lectura = sensor.obtener_lectura()
            datos[sensor.tipo] = lectura
            # resultados.append(resultado)
        return datos




administrador = AdministradorSensores()
administrador.agregar_sensor(SensorTemperatura())
administrador.agregar_sensor(SensorGas())
administrador.agregar_sensor(SensorMovimiento())
administrador.agregar_sensor(CamaraSeguridad())



try:
    while True:
        resultados = administrador.operar()
        if "temperatura" in resultados:
            print(f"Temperatura detectada: {resultados['temperatura']} grados.")
        if "gas" in resultados:
            print(f"Nivel de gas: {resultados['gas']} ppm.")
        if "movimiento" in resultados:
            print(f"Movimiento detectado: {resultados['movimiento']}.")
        if "camara" in resultados:
            print(f"Cámara funcionando: {resultados['camara']}.")    
        time.sleep(15)


except KeyboardInterrupt:
    print("Sistema desactivado")
