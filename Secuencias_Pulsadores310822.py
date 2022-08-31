from time import sleep
from machine import Pin as pin 
from utime import sleep as pausa, sleep_ms as pausam

#leds
led1=pin(22,pin.OUT)  # LED BLANCO      1    1
led2=pin(19,pin.OUT)  # LED ROJO        1    2 
led3=pin(23,pin.OUT)  # LED AMARILLO    1    3
led4=pin(1,pin.OUT)   # LED AZUL        1    4 
led5=pin(21,pin.OUT)  # LED VERDE       1    5
led6=pin(18,pin.OUT)  # LED AMARILLO    2    6
led7=pin(17,pin.OUT)  # LED AZUL        2    7
led8=pin(4,pin.OUT)   # LED VERDE       2    8
led9=pin(2,pin.OUT)   # LED BLANCO      2    9
led10=pin(15,pin.OUT) # LED ROJO        2    10
#botones
btn_Verde=pin(16,pin.IN)
btn_Amarillo=pin(13,pin.IN)
btn_Azul=pin(12,pin.IN)
btn_Rojo=pin(14,pin.IN)
btn5=pin(26,pin.IN)

LEDcol=[led3,led6,led4,led7,led2,led10]
LEDorden=[led1,led2,led3,led4,led5,led6,led7,led8,led9,led10]
LEDfha=[led1,led10,led2,led9,led3,led8,led4,led7,led5,led6]
LEDxC=[led1,led9,led2,led10,led3,led6,led4,led7,led5,led8] #blanco - rojo - amarillo - azul - verde
LEDPARY=[led5,led1,led10,led2,led9,led3,led8]

pausa =0.1


def secuencia1(): #hacia derecha
    LEDiniciales = LEDorden
    for elemento in LEDiniciales:
        elemento.value(1)
        sleep(pausa)
        elemento.value(0)
        sleep(pausa)
    
def secuencia2(): #hacia izquierda
    LEDfinales = LEDorden[::-1]
    for elemento in LEDfinales:
        elemento.value(1)
        sleep(pausa)
        elemento.value(0)
        sleep(pausa)
                
def secuencia3(): #pares
    LEDpares = LEDorden[::2]
    for elemento in LEDpares:
        elemento.value(1)
        sleep(pausa)
        elemento.value(0)
        sleep(pausa)
        
def secuencia4(): #impares
    LEDimpares = LEDorden[1::2]
    for elemento in LEDimpares:
        elemento.value(1)
        sleep(pausa)
        elemento.value(0)
        sleep(pausa)
        
        
def secuencia5(): #hacia dentro
    LEDdentro= LEDfha
    for elemento in LEDdentro:
        elemento.value(1)
        sleep(pausa)
        elemento.value(0)
        sleep(pausa)


def secuencia6(): #haica fuera
    LEDfuera= LEDfha[::-1]
    for elemento in LEDfuera:
        elemento.value(1)
        sleep(pausa)
        elemento.value(0)
        sleep(pausa)
    
def secuencia7(): #blanco - rojo - amarillo - azul - verde
    LEDcolores = LEDxC
    for elemento in LEDcolores:
        elemento.value(1)
        sleep(pausa)
        elemento.value(0)
        sleep(pausa)

def secuencia8(): #Prenden todos los leds y se devuelve sin tocar extremos
    LEDmitad = LEDorden[1:-1]
    for i in LEDmitad:
        i.value(1)
        sleep(pausa)
        i.value(0)
        sleep(pausa)
    LEDmitad = LEDorden[8:0:-1]
    for i in LEDmitad:
        i.value(1)
        sleep(pausa)
        i.value(0)
        sleep(pausa)
        
def secuencia9(): #Alumbran los led en orden de los colores de la bandera de colombia
    LED9 = LEDcol
    for i in LED9:
        i.value(1)
        sleep(pausa)
        i.value(0)
        sleep(pausa)

def secuencia10(): #Alumbran los leds en reversa a la bandera de colombia
    LED10 = LEDcol
    for i in reversed(LED10):
        i.value(1)
        sleep(pausa)
        i.value(0)
        sleep(pausa)

def secuencia11():#Se borran los leds amarillos y se encienden los colores restantes a la bandera de colombia
    LED11 = LEDcol[2:]
    for i in LED11:
        i.value(1)
        sleep(pausa)
        i.value(0)
        sleep(pausa)

def secuencia12(): #colores calidos: prende solo los leds rojos y amarillos
    LEDcalido = LEDxC[2:5:]
    for elemento in LEDcalido:
        elemento.value(1)
        sleep(pausa)
        elemento.value(0)
        sleep(pausa)
     
def secuencia13(): #Alumbran los leds rojo y luego azul como policia
    LED12 = LEDcol[2:]
    for i in reversed (LED12):
        i.value(1)
        sleep(pausa)
        i.value(0)
        sleep(pausa)

def secuencia14(): #Prenden los leds desde el medio y desde los ls laterales hacia dentro
    LED13 = LEDPARY
    for i in LED13:
        i.value(1)
        sleep(pausa)
        i.value(0)
        sleep(pausa)

    LED13 = LEDPARY
    for i in reversed (LED13):
        i.value(1)
        sleep(pausa)
        i.value(0)
        sleep(pausa)

def secuencia15(): #colores frios: prende solo los leds azules y verdes
        LEDfrio = LEDxC[6:9:]
        for elemento in LEDfrio:
            elemento.value(1)
            sleep(pausa)
            elemento.value(0)
            sleep(pausa)    

#Main
while True:
    btn_Verde.value(0)
    btn_Amarillo.value(0)
    btn_Azul.value(0)
    btn_Rojo.value(0)
    btn5.value(0)
    
    dato=0
    dato=btn_Verde.value()+btn_Amarillo.value()*2+btn_Azul.value()*4+btn_Rojo.value()*8
    print(dato)
    sleep(0.5)
    
    if dato == 1:
        secuencia1()
        
    if dato == 2:
        secuencia2()
        
    if dato == 3:
        secuencia3()
        
    if dato == 4:
        secuencia4()

    if dato == 5:
        secuencia5()

    if dato == 6:
        secuencia6()

    if dato == 7:
        secuencia7()

    if dato == 8:
        secuencia8()

    if dato == 9:
        secuencia9()

    if dato == 10:
        secuencia10()

    if dato == 11:
        secuencia11()

    if dato == 12:
        secuencia12()

    if dato == 13:
        secuencia13()

    if dato == 14:
        secuencia14()

    if dato == 15:
        secuencia15()
    
    if (btn5.value()==1):
        pausa=pausa+0.1
        print("tiempo")
    if (btn5.value()==0):
        pausa=0.1
        print("tiempo")
