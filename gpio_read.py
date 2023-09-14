import OPi.GPIO as GPIO
import time

class opi_gpio:

    def gpio_init(channel):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

    def read_button_init(channel):
        GPIO.setup(channel, GPIO.IN)
    
    def read_button(channel, bounctime, callback):
        if not GPIO.input(channel):
            time.sleep(bounctime)
            if not GPIO.input(channel):
                return callback()
            
        return None

    def out_init(channel):
        GPIO.setup(channel, GPIO.OUT)
        GPIO.output(channel, GPIO.LOW) 

    def blink_led(channel):
        for i in range(4):
            GPIO.output(channel, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(channel, GPIO.LOW)
            time.sleep(0.5)

    def light_led(channel):
       GPIO.output(channel, GPIO.HIGH)
       time.sleep(3)
       GPIO.output(channel, GPIO.LOW) 

def my_callback():
    print('This is a edge event callback function!')
    print('Edge detected on channel')
    print('This is run in a different thread to your main program')

def test():
    opi_gpio.gpio_init(12)
    opi_gpio.read_button_init(12)
    opi_gpio.read_button(12, 1, my_callback) 
    opi_gpio.gpio_init(16)
    opi_gpio.out_init(16)
    opi_gpio.blink_led(16)

if __name__ == "__main__":
    test()
        