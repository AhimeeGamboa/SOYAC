import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import threading
import time
import sys

#Clase proceso
class Proceso:
    def __init__(self, pid, nombre, tiempo_rafaga):
        self.pid = pid
        self.nombre = nombre
        self.estado = "Listo"
        self.tiempo_restante = tiempo_rafaga

#Clase sistema operativo
class SistemaOperativo:
    def __init__(self):
        self.peocesos = {}
        self.siguiente_pid = 1
    
    def crear_proceso (self, nombre, tiempo_rafaga):
        proceso = Proceso (self.siguiente_pid, nombre, tiempo_rafaga)
        self.procesos [self.siguiente_pid] = proceso

        print (f"Proceso creado -> PID: {proceso.pid}, Nombre: {proceso.nombre}")

        self.siguiente_pid += 1

    def eliminar_proceso (self, pid):
        if pid in self.procesos:
            print(f"Proceso eliminado -> PID: {pid}")
        else:
            print("ERROR: PID no encontrado")

    def ejecutar_unidad_tiempo(self):
        #Buscar el primer proceso no terminado
        for proceso in self.procesos.values():

            if proceso.tiempo_restante > 0:

                proceso.estado = "Ejecutando"
                proceso.tiempo_restante -= 1

                print(f"Ejecutando PID {proceso.pid}" f"- Tiempo restante: {proceso.tiempo_restante}")

                #verificar si terminó
                if proceso.tiempo_restante == 0:
                    proceso.estado = "Terminado"
                    print(f"Proceso {proceso.pid} terminado")
                break