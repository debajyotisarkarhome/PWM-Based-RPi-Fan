# PWM Based RPi Fan
A really nifty script for Optimal Cooling on the Raspberry Pi Based on Real Time Temperature Values From Raspberry Pi 4 (2020).

Just fun This code as service and forget About Overheating

**Shopping List :**
1. A 5V DC Raspberry Pi Cooling Fan.
2. A BC547 Transistor or any General Purpose NPN Transistor. (Rating More than 100mA recommended)
3. Some jumper Wires

**Wiring The Fan :**

<img align="centre" alt="Schematic" src="https://user-images.githubusercontent.com/42748272/100542054-e7feed80-326d-11eb-9144-130fd093f6bc.jpg"/>

**Running as a service** 

Place the "FanCon.py" file in the home/pi/ directory and then copy the fancon.service file to /etc/systemd/system/.
Then Open Terminal And Type in the following Command:

> sudo systemctl enable fancon.service


