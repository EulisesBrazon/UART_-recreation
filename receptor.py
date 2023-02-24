import machine
import time

espera = 0.3 #tiempo de demora para las pulsaciones de los botones en segundos
retardo = 1000 #tiempo de retardo en la señal uart, entre el envio de cada bit (en ms)
prudentTime = int(retardo/2)
pinRx = 17 #pin para la recepcion de informacion
rx = machine.Pin(pinRx,machine.Pin.IN, machine.Pin.PULL_DOWN)#inicializando el pin rx

#inicializando los 8 leds para mostrar el valor de cada bit
led0 = machine.Pin(6,machine.Pin.OUT)
led1 = machine.Pin(7,machine.Pin.OUT)
led2 = machine.Pin(9,machine.Pin.OUT)
led3 = machine.Pin(10,machine.Pin.OUT)
led4 = machine.Pin(12,machine.Pin.OUT)
led5 = machine.Pin(13,machine.Pin.OUT)
led6 = machine.Pin(14,machine.Pin.OUT)
led7 = machine.Pin(15,machine.Pin.OUT)

#cargando las de claraciones en un unico arreglo
salida = [led0,led1,led2,led3,led4,led5,led6,led7]

def reciveByte():
    array = ""
    #se evalua y almacena el resultado
    for i in range (8):
        if rx.value()==1:
            array += "1"
        else:
            array += "0"
        #se espera a que lelgue el proximo byte
        time.sleep_ms(retardo)
    return array

#para asegurar que todos los leds esten apagados antes de iniciar
def turnOffLed():
    for i in range (8):
        salida[i].value(0)
        
def receiver():
    turnOffLed()
    while True:
        if rx.value()==0:
            print('Recibiendo informacion')
            #espera de tiempo prudente para empezar la lectura en un punto estable
            time.sleep_ms(retardo)
            time.sleep_ms(prudentTime)
            #carga del byte
            dateReceiver=reciveByte()
            print('orden de los datos recibidos'+str(datoEviar))
            #utilizo la informazion para encernder los leds
            for i in range(len(dateReceiver)):
                if dateReceiver[i]=='1':
                    salida[i].value(1)                                            
                else:
                    salida[i].value(0)

def main():
    while True :
        try:
            receiver()
        except Exception as e:
            print("Error:", e)
        
if __name__ == '__main__':
    main()
    