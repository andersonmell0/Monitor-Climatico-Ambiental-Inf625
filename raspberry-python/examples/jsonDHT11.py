# Programa : Sensor de temperatura DHT11 com Raspberry Pi B+
 
# Carrega as bibliotecas
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import json

# Define o tipo de sensor
sensor = Adafruit_DHT.DHT11
 
GPIO.setmode(GPIO.BOARD)
 
# Define a GPIO conectada ao pino de dados do sensor
pino_sensor = 25

class ObterDados():
   # Informacoes iniciais
   print ("*** Obtendo Data, Temperatura e Umidade");
   while(1):
      # Efetua a leitura do sensor
      umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor)
      # Caso leitura esteja ok, mostra os valores na tela
      if umid is not None and temp is not None:
         #Converte os dados em json
         str_dados = {'Data' : time.strftime('%d %b %y %H:%M:%S') , 'Temperatura': temp, 'Umidade': umid }
         json_str = json.dumps(str_dados, indent=4)
         print json_str
         #Salva em arquivo json
         try:
            arquivo_json = open("teste.json", "w")
            arquivo_json.write(json_str)
            arquivo_json.close()
            #with open("teste.json", "w") as write_file:
               #json.dump(json_str, write_file)
         except Exception as erro:
            print('Erro ao gravar no arquivo:{}'.format(erro))
            
         print ("Efetuando Nova Leitura ...");
         time.sleep(30)
      else:
         # Mensagem de erro de comunicacao com o sensor
         print("Falha ao ler dados do DHT11 !!!")
