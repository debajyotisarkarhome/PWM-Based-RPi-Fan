import RPi.GPIO as GPIO
from time import sleep
import subprocess

ledpin = 12				
GPIO.setwarnings(False)			
GPIO.setmode(GPIO.BOARD)		
GPIO.setup(ledpin,GPIO.OUT)
pi_pwm = GPIO.PWM(ledpin,1000)		
pi_pwm.start(0)				 
while True:
        out = subprocess.Popen(['vcgencmd', 'measure_temp'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout,stderr = out.communicate()
        tp=stdout.decode("UTF-8")
        tp=tp.replace("temp=","")
        tp=tp.replace("'C\n","")
        tp=float(tp)
        tp=int(tp)
	#pun=input("Enter DC value[0-100]")
        if tp<=45:
                pi_pwm.ChangeDutyCycle(60)
        elif tp>45 and tp<=50:
                pi_pwm.ChangeDutyCycle(80)
        elif tp>50 and tp<=60:
                pi_pwm.ChangeDutyCycle(90)
        elif tp>60:
                pi_pwm.ChangeDutyCycle(100)
        sleep(20)

