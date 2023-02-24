import machine
import time

espera = 0.3 #tiempo de demora para las pulsacione de los botones en segundos
retardo = 1000 #tiempo de retardo en la señal uart, en el envio de cada bit (en ms)
pinTx = 0 #pin para el envio de la informacion
tx = machine.Pin(pinTx,machine.Pin.OUT)
buttonSend = machine.Pin(3,machine.Pin.IN, machine.Pin.PULL_DOWN)

button0 = machine.Pin(8,machine.Pin.IN, machine.Pin.PULL_DOWN)
button1 = machine.Pin(9,machine.Pin.IN, machine.Pin.PULL_DOWN)
button2 = machine.Pin(10,machine.Pin.IN, machine.Pin.PULL_DOWN)
button3 = machine.Pin(11,machine.Pin.IN, machine.Pin.PULL_DOWN)
button4 = machine.Pin(12,machine.Pin.IN, machine.Pin.PULL_DOWN)
button5 = machine.Pin(13,machine.Pin.IN, machine.Pin.PULL_DOWN)
button6 = machine.Pin(14,machine.Pin.IN, machine.Pin.PULL_DOWN)
button7 = machine.Pin(15,machine.Pin.IN, machine.Pin.PULL_DOWN)

led0 = machine.Pin(16,machine.Pin.OUT)
led1 = machine.Pin(17,machine.Pin.OUT)
led2 = machine.Pin(18,machine.Pin.OUT)
led3 = machine.Pin(19,machine.Pin.OUT)
led4 = machine.Pin(21,machine.Pin.OUT)
led5 = machine.Pin(22,machine.Pin.OUT)
led6 = machine.Pin(26,machine.Pin.OUT)
led7 = machine.Pin(27,machine.Pin.OUT)

isOn0 = False
isOn1 = False
isOn2 = False
isOn3 = False
isOn4 = False
isOn5 = False
isOn6 = False
isOn7 = False

entrada = [button0,button1,button2,button3,button4,button5,button6,button7]
salida = [led0,led1,led2,led3,led4,led5,led6,led7]
estadoLed = [isOn0,isOn1,isOn2,isOn3,isOn4,isOn5,isOn6,isOn7]

def sendByte(char):
   #arreglo = completar_ceros(decimal_to_binary(ord(char)))
    arreglo = char
    print('enviando informacion'+str(arreglo))
    tx.off()#se envia el primer bit de aviso
    
    print('primer bit de aviso')
    time.sleep_ms(retardo)
    #se envia los siguientes 8 bits
    contador = 0
    for i in arreglo:
        #dependiendo del valor, se cambia el estado del la linea
        if(i==True):
            print('enviando el bit ' + str(contador) + ' con el valor '+ str(i))
            tx.on()
            time.sleep_ms(retardo)
        else:
            print('enviando el bit ' + str(contador) + ' con el valor '+ str(i))
            tx.off()
            time.sleep_ms(retardo)
        contador += contador 
    pinTx.on()#estado de reposo
    time.sleep_ms(retardo)#tiempo prudente antes de poder enviar otro byte

#para asegurar que todos los leds esten apagados antes de iniciar
def turnOffLed():
    for i in range (8):
        salida[i].value(0)

def emisor():
    turnOffLed()
    while True:
        #se recorre las entradas para saber si algun boton a sido precionado
        for i in range (8):
            if entrada[i].value()==1:
                estadoLed[i] = not estadoLed[i]
                salida[i].value(estadoLed[i])
                print('el boton '+ str(i) + ' a sido precionado')
                time.sleep(espera)
        #si el boton de envio se preciono, se procede a enviar la informacio
        if buttonSend.value()==1:
            print('enviando informacion')
            time.sleep(espera)
            sendByte(estadoLed)
                                        
def main():
    while True :
        try:
            emisor()
        except Exception as e:
            print("Error:", e)    

if __name__ == '__main__':
    main()                                

    

        
