import RPi.GPIO as GPIO

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
x = GPIO.PWM(24, 1000)
x.start(0)

try:
    while True:
        q = int(input("Введите число: "))
        x.ChangeDutyCycle(q)
finally:
    GPIO.cleanup()