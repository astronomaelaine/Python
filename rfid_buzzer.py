import os
import sys
import signal
import time

#    Lista com relacao dos IDs autorizados 
acessos_autorizados = [[83,196,103,154,106]]
#
#    Vou tentar importar os modulos abaixo, caso algum problema ocorra,
#    sera lancada a excecao na sequencia

try:
    import MFRC522
    import RPi.GPIO as GPIO
except ImportError as ie:
    print("Problema ao importar modulo {0}").format(ie)
    sys.exit()
 

#    Funcao que ira garantir que o root ou usuario com permissao de
#    super-usuario ira executar a aplicacao

def check_user():
    if os.geteuid() != 0:
        print("Voce deve executar o programa como super-usuario!")
        #print "Exemplo:\nsudo python {0}".format(os.path.realpath(__file__))
        print("Exemplo:\nsudo python {0}").format(__file__)
        sys.exit()
 
 
#
#    Captura o sinal gerado, no caso o que nos interessa e o sinal
#    SIGINT(Interrupcao do Terminal ou processo) e ira encerrar a aplicacao

def finalizar_app(signal,frame):
    global continue_reading
    print("\nCtrl+C pressionado, encerrando aplicacao...")
    continue_reading = False

    GPIO.cleanup()

 
GPIO.setmode(GPIO.BOARD)
continue_reading = True
#GPIO.setup(8, GPIO.OUT)
#GPIO.setup(10, GPIO.OUT)

#GPIO.output(8, 1)
#GPIO.output(10, 0)

red = 12
blue = 8
green = 16
buzzer = 7

def initGpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(green, GPIO.OUT) #Led verde
    GPIO.setup(red, GPIO.OUT) #Led vermelho
    GPIO.setup(blue, GPIO.OUT) #Led azul
    GPIO.setup(buzzer, GPIO.OUT) #Buzzer
    GPIO.output(green, 0)
    GPIO.output(red, 0)
    GPIO.output(buzzer, 0)
    GPIO.output(blue, 1)

def redOn():
    GPIO.output(blue, 0)
    GPIO.output(red, True)
    GPIO.output(buzzer, True)
    time.sleep(0.1)
    GPIO.output(buzzer, False)
    GPIO.output(red, False)
    time.sleep(0.1)
    GPIO.output(buzzer, True)
    GPIO.output(red, True)
    time.sleep(0.1)
    GPIO.output(red, False)
    GPIO.output(buzzer, False)
    GPIO.output(blue, 1)

def greenOn():
    GPIO.output(blue, 0)
    GPIO.output(green,True)
    GPIO.output(buzzer,True)
    time.sleep(0.3)
    GPIO.output(green,False)
    GPIO.output(buzzer,False)
    GPIO.output(blue, 1)

def main():
 
    check_user()
    initGpio()
 
    # Handler do sinal SIGINT
    signal.signal(signal.SIGINT, finalizar_app)
 
    # Cria o objeto da class MFRC522
    MIFAREReader = MFRC522.MFRC522()
 
    print("Portal Embarcados - Python sucesso!")
    print("Pressione Ctrl-C para encerrar a aplicacao.")
 
    while continue_reading:
	
        # Scan for cards    
        #(status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
        MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
 
 
        # Get the UID of the card
        (status,uid) = MIFAREReader.MFRC522_Anticoll()
 
        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:
            if uid in acessos_autorizados:
                print("Acesso liberado!")
                greenOn()
		    		    #GPIO.output(10, 1)
		    #time.sleep(1) 
		    #GPIO.output(10, 0)
            else:
                print "Card read UID: " + str(uid[0]) + "," + str(uid[1]) + "," + str(uid[2]) + "," + str(uid[3])
                print("Sem acesso!")
                redOn()

if __name__ == "__main__":
    main()

GPIO.cleanup()
