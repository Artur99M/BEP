import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
    
def bin2dec(bin):
    bin = bin[::-1]
    a = 0
    for i in range(len(bin)):
        a += bin[i] * (2**i)
    return a
dac    = [8, 11, 7, 1, 0, 5, 12, 6]
comp   = 14
troyka = 13
leds   = [9, 10, 22, 27, 17, 4, 3, 1]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

def adc():
    a = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(a)):
        a[i] = 1
        GPIO.output(dac, a)
        time.sleep(0.001)
        comp_value = GPIO.input(comp)
        if comp_value == 1:
            a[i] = 0
    return bin2dec(a)

        

try:
    while True:
        v = adc()
        a = dec2bin(v)
        if v != 0:
            jls_extract_var = "{:.4f}"
            print(jls_extract_var.format(v * 3.3 / 255))
        GPIO.output(leds, a)

finally:
    GPIO.output (dac, 0)
    GPIO.cleanup()