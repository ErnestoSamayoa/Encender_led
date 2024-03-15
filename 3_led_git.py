import serial
from serial.tools.list_ports import comports
from time import sleep
from tkinter import *

estadoLed1 = 0
estadoLed2 = 0
estadoLed3 = 0

def setup():
    global puerto
    puerto = serial.Serial(comports()[0].device, 9600)
    sleep(2)  # Espera a que se establezca la conexión

def draw():
    global estadoLed1, estadoLed2, estadoLed3
    canvas.delete("all")  # Borra todo el contenido anterior
    if estadoLed1 == 0:
        canvas.create_oval(50, 50, 100, 100, fill="red")
    elif estadoLed1 == 1:
        canvas.create_oval(50, 50, 100, 100, fill="#F4FFA5")
    
    if estadoLed2 == 0:
        canvas.create_oval(150, 50, 200, 100, fill="green")
    elif estadoLed2 == 1:
        canvas.create_oval(150, 50, 200, 100, fill="#F4FFA5")
    
    if estadoLed3 == 0:
        canvas.create_oval(250, 50, 300, 100, fill="yellow")
    elif estadoLed3 == 1:
        canvas.create_oval(250, 50, 300, 100, fill="#F4FFA5")

def toggle_leds():
    global estadoLed1, estadoLed2, estadoLed3
    estadoLed1 = 1 - estadoLed1  # Cambia el estado del LED 1
    estadoLed2 = 1 - estadoLed2  # Cambia el estado del LED 2
    estadoLed3 = 1 - estadoLed3  # Cambia el estado del LED 3
    puerto.write(b'1' if estadoLed1 else b'0')  # Envía el estado del LED 1 al Arduino
    puerto.write(b'2' if estadoLed2 else b'3')  # Envía el estado del LED 2 al Arduino
    puerto.write(b'4' if estadoLed3 else b'5')  # Envía el estado del LED 3 al Arduino
    draw()

# Configuración de la ventana
root = Tk()
width = 350
height = 150
root.geometry(f"{width}x{height}")
canvas = Canvas(root, width=width, height=height)
canvas.pack()

setup()

toggle_button = Button(root, text="Toggle LEDs", command=toggle_leds)
toggle_button.place(x=130, y=120)  # Coloca el botón en la ventana

draw()

root.mainloop()