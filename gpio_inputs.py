#!/usr/bin/env python2
# -*- coding: utf-8 -*-
 
import RPi.GPIO as GPIO
import time
import os
 
#
# Einstellungen
#
 
# GPIO-Bezeichnungien (BCM) im Skript verwenden
GPIO.setmode(GPIO.BCM)
 
# Angeschlossene GPIOs
in_a = 17
in_b = 6
in_c = 24
 
# Bash-Kommandos, die bei Aktivierung eines GPIOs ausgeführt werden
# Doppelte Anführungsstriche müssen mit \ excaped werden!
cmd_a = "echo -n 'input1' > /dev/udp/192.168.3.210/7010"
cmd_b = "echo -n 'input2' > /dev/udp/192.168.3.210/7010 && /usr/bin/amixer cset numid=1 -- -400 && /usr/bin/aplay ./klingelsound.wav"
cmd_c = ""

# Interne Pullup-/Pulldown-Widerstaende einschalten
# Bei Verschaltung gegen GND: GPIO.PUD_UP
# Bei Verschaltung gegen +3.3V: GPIO.PUD_DOWN
pullupdown_in_a = GPIO.PUD_DOWN
pullupdown_in_b = GPIO.PUD_DOWN
pullupdown_in_c = GPIO.PUD_UP
 
# Bounce-Zeit in ms
bouncetime = 250
 
#
# Einstellungen Ende
#
 
# GPIO Settings
GPIO.setup(in_a, GPIO.IN, pull_up_down = pullupdown_in_a)
GPIO.setup(in_b, GPIO.IN, pull_up_down = pullupdown_in_b)
GPIO.setup(in_c, GPIO.IN, pull_up_down = pullupdown_in_c)

if pullupdown_in_a == GPIO.PUD_UP:
    edge_in_a = GPIO.FALLING
else:
    edge_in_a = GPIO.RISING
if pullupdown_in_b == GPIO.PUD_UP:
    edge_in_b = GPIO.FALLING
else:
    edge_in_b = GPIO.RISING
if pullupdown_in_c == GPIO.PUD_UP:
    edge_in_c = GPIO.FALLING
else:
    edge_in_c = GPIO.RISING

# Input 1
def Input1(channel):
    print "Input 1 aktiviert"
    os.system('bash -c \"cmd_a\"')
 
# Input 2
def Input2(channel):
    print "Input 2 aktiviert"
 
# Input 3
def Input3(channel):
    print "Input 3 aktiviert"
 
# Interrupts
GPIO.add_event_detect(in_a, edge_in_a, callback = Input1, bouncetime = bouncetime)
GPIO.add_event_detect(in_b, edge_in_b, callback = Input2, bouncetime = bouncetime)
GPIO.add_event_detect(in_c, edge_in_c, callback = Input3, bouncetime = bouncetime)
 
# Schleife
try:
    while True:
        time.sleep(1)
 
except:
  GPIO.cleanup()
  print "\nBye"
