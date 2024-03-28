import RPi.GPIO as GPIO
import time

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        time.sleep(2)
        q = input("End or no: ")
        period = input ("print priod: ")
        period = int(period)
        if q == "end":
            break
        t = 0
        while t < 255:
            time.sleep(period/1000)
            GPIO.output(dac, decimal2binary(t))
            t += 1
        while t > 0:
            time.sleep(period/1000)
            GPIO.output(dac, decimal2binary(t))
            t -= 1
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()