import RPi.GPIO as GPIO

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        num = input ("Print a number 0-255: ")
        try:
            num = int(num)
            if 0 <= num <=255:
                GPIO.output (dac, decimal2binary(num))
                print ("{:.4f}".format(num*3.3/255))
            else:
                print ("You have to print a int number 0-255")
        except Exception:
            if num == "q":
                break
            print ("You have to print a number")


finally:
    GPIO.output (dac, 0)
    GPIO.cleanup()