import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

class Device:
    def __init__(self, topic, mqtt_broker='localhost', port=2000):
        self.topic = topic
        
        self.topic_list = self.topic.split('/')
        
        self.location = self.topic_list[0]
        self.group = self.topic_list[1]
        self.device_type = self.topic_list[2]
        self.device_name = self.topic_list[3]
        
        self.mqtt_broker = mqtt_broker
        self.port = port
        
        self.connect_mqtt()
        self.setup_gpio()
        

    def connect_mqtt(self):
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.connect(self.mqtt_broker, self.port)
        
    def setup_gpio(self):
        GPIO.setmode(GPIO.BCM)
        
        if self.device_type == 'lamps':
            GPIO.setup(17, GPIO.OUT)
            
        elif self.device_type == 'doors':
            GPIO.setup(27, GPIO.OUT)
            
        elif self.device_type == 'fans':
            GPIO.setup(22, GPIO.OUT)
        
        elif self.device_type == 'camera':
            GPIO.setup(100, GPIO.OUT)
        
    def turn_on(self):
        self.send_commands('TURN_ON') 
        print(' Turned on succesfully.')
        
        if self.device_type == 'camera':
            print("Camera is now recording")
    
    def turn_off(self):
        self.send_commands('TURN_OFF')
        print('Turned off succesfully.')
        
        if self.device_type == 'camera':
            print("Camera recording stopped")
    
    def send_commands(self, command):
        self.mqtt_client.publish(self.topic, command)   
        print('done')


a1=Device(topic='home/living_room/cameras/camera2',mqtt_broker='....', port='2000')
