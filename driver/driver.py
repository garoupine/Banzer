from pyPS4Controller.controller import Controller
import RPi.GPIO as GPIO  
import time

    
class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        

    def on_L3_up(self, value):
    
        if value < -5000:
            GPIO.output(22, GPIO.LOW)
            p4.ChangeDutyCycle(0)
            GPIO.output(23, GPIO.HIGH)
            p3.ChangeDutyCycle(-value/32768*100/4)
            
        elif value > 5000:
            GPIO.output(23, GPIO.LOW)
            p3.ChangeDutyCycle(0)
            GPIO.output(22, GPIO.HIGH)
            p4.ChangeDutyCycle(value/32768*100/4)
        
        elif value < 5000 and value > -5000:
            GPIO.output(23,GPIO.LOW)
            GPIO.output(22,GPIO.LOW)
            p4.ChangeDutyCycle(0)
            p3.ChangeDutyCycle(0)           
               
    def on_L3_down(self, value):
        
        if value < -5000:
            GPIO.output(22, GPIO.LOW)
            p4.ChangeDutyCycle(0)
            GPIO.output(23, GPIO.HIGH)
            p3.ChangeDutyCycle(-value/32768*100/4)
            
        elif value > 5000:
            GPIO.output(23, GPIO.LOW)
            p3.ChangeDutyCycle(0)
            GPIO.output(22, GPIO.HIGH)
            p4.ChangeDutyCycle(value/32768*100/4)
        
        elif value < 5000 and value > -5000:
            GPIO.output(23,GPIO.LOW)
            GPIO.output(22,GPIO.LOW)
            p4.ChangeDutyCycle(0)
            p3.ChangeDutyCycle(0)
  

    def on_R3_up(self, value):
    
        if value < -5000:
            GPIO.output(20, GPIO.LOW)
            p2.ChangeDutyCycle(0)
            GPIO.output(26, GPIO.HIGH)
            p.ChangeDutyCycle(-value/32768*100/2)
            
        elif value > 5000:
            GPIO.output(26, GPIO.LOW)
            p.ChangeDutyCycle(0)
            GPIO.output(20, GPIO.HIGH)
            p2.ChangeDutyCycle(value/32768*100/2)
            
        elif value < 5000 and value > -5000:
            GPIO.output(20,GPIO.LOW)
            GPIO.output(26,GPIO.LOW)
            p.ChangeDutyCycle(0)
            p2.ChangeDutyCycle(0)
            
               
    def on_R3_down(self, value):
    
        if value < -5000:
            GPIO.output(20, GPIO.LOW)
            p2.ChangeDutyCycle(0)
            GPIO.output(26, GPIO.HIGH)
            p.ChangeDutyCycle(-value/32768*100/2)
            
        elif value > 5000:
            GPIO.output(26, GPIO.LOW)
            p.ChangeDutyCycle(0)
            GPIO.output(20, GPIO.HIGH)
            p2.ChangeDutyCycle(value/32768*100/2)
            
        elif value < 5000 and value > -5000:
            GPIO.output(20,GPIO.LOW)
            GPIO.output(26,GPIO.LOW)
            p.ChangeDutyCycle(0)
            p2.ChangeDutyCycle(0)
            
            
            

##initsection
GPIO.setmode(GPIO.BCM)
#First Motor 
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
#Second Motor
GPIO.setup(19, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

#PWM Signals 
#First motor
p = GPIO.PWM(12, 50)  # frequency=50Hz
p.start(0)
p2 = GPIO.PWM(13, 50)  # frequency=50Hz
p2.start(0)
#Second motor
p3 = GPIO.PWM(19, 50)  # frequency=50Hz
p3.start(0)

p4 = GPIO.PWM(18, 50)  # frequency=50Hz
p4.start(0)

'''
try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
    p.stop()
    GPIO.cleanup()
'''    

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window

##codesection
controller.listen(timeout=6000)


