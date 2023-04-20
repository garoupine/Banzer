from pyPS4Controller.controller import Controller
import RPi.GPIO as GPIO  
    
class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
       GPIO.output(17, GPIO.HIGH)

    def on_x_release(self):
       GPIO.output(17, GPIO.LOW)

    def on_triangle_press(self):
        GPIO.output(23, GPIO.HIGH)

    def on_triangle_release(self):
        GPIO.output(23, GPIO.LOW)
    
    def on_square_press(self):
        GPIO.output(27, GPIO.HIGH)
	
    def on_square_release(self):
        GPIO.output(27, GPIO.LOW)

    def on_circle_press(self):
        GPIO.output(22, GPIO.HIGH)
	    
    def on_circle_release(self):
        GPIO.output(22, GPIO.LOW)

##initsection
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window

##codesection
controller.listen()



