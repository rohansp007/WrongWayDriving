from gpiozero import Buzzer
from time import sleep

buz = Buzzer(16)

def buzz():
        buz.on()
        sleep(1)
        buz.off()
        sleep(1)

buzz()
