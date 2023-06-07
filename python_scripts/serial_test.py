import serial
import time

SerialObj = serial.Serial('/dev/ttyUSB0')
time.sleep(0.1)
SerialObj.timeout = 1

while True:
    if SerialObj.is_open:  # Verifica si el puerto serie está abierto
        try:
            ReceivedString = SerialObj.readall() 
            if ReceivedString:  # Verifica si se ha recibido alguna información
                print(ReceivedString)
        except serial.SerialException:  # Captura la excepción si se produce un error en la lectura
            print("Error al leer los datos del puerto serie.")
            break  # Detiene el bucle en caso de que ocurra un error
    else:
        print("El puerto serie está cerrado.")
        break  # Detiene el bucle si el puerto serie está cerrado
        
SerialObj.close()
