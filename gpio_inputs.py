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
in_b = 27
in_c = 23
in_d = 24
in_e = 25
 
# Bash-Kommandos, die bei Aktivierung eines GPIOs ausgeführt werden
# Doppelte Anführungsstriche müssen mit \ escaped werden!
cmd_a = "echo -n 'input1' > /dev/udp/192.168.3.210/7010 && echo 'UDP Paket gesendet'"
cmd_b = "echo -n 'input2' > /dev/udp/192.168.3.210/7010 && /usr/bin/amixer cset numid=1 -- -400 && /usr/bin/aplay ./klingelsound.wav && echo 'UDP Paket gesendet'"
cmd_c = ""
cmd_d = ""
cmd_e = ""

# Interne Pullup-/Pulldown-Widerstaende einschalten
# Bei Verschaltung gegen GND: GPIO.PUD_UP
# Bei Verschaltung gegen +3.3V: GPIO.PUD_DOWN
pullupdown_in_a = GPIO.PUD_DOWN
pullupdown_in_b = GPIO.PUD_DOWN
pullupdown_in_c = GPIO.PUD_UP
pullupdown_in_d = GPIO.PUD_UP
pullupdown_in_e = GPIO.PUD_UP
 
# Bounce-Zeit in ms
bouncetime = 300
 
#
# Einstellungen Ende
#
 
# GPIO Settings
GPIO.setup(in_a, GPIO.IN, pull_up_down = pullupdown_in_a)
GPIO.setup(in_b, GPIO.IN, pull_up_down = pullupdown_in_b)
GPIO.setup(in_c, GPIO.IN, pull_up_down = pullupdown_in_c)
GPIO.setup(in_d, GPIO.IN, pull_up_down = pullupdown_in_c)
GPIO.setup(in_e, GPIO.IN, pull_up_down = pullupdown_in_c)

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

if pullupdown_in_d == GPIO.PUD_UP:
    edge_in_d = GPIO.FALLING
else:
    edge_in_d = GPIO.RISING

if pullupdown_in_e == GPIO.PUD_UP:
    edge_in_e = GPIO.FALLING
else:
    edge_in_e = GPIO.RISING

# Input 1
def Input1(channel):
    print "--> Input 1 <--"
    print "Command: ", cmd_a
    os.system('bash -c "' + cmd_a + '"')
 
# Input 2
def Input2(channel):
    print "--> Input 2 <--"
    print "Command: ", cmd_b
    os.system('bash -c "' + cmd_b + '"')
 
# Input 3
def Input3(channel):
    print "--> Input 3 aktiviert <--"
    print "Command: ", cmd_c
    os.system('bash -c "' + cmd_c + '"')
 
# Input 4
def Input4(channel):
    print "--> Input 4 aktiviert <--"
    print "Command: ", cmd_d
    os.system('bash -c "' + cmd_d + '"')

# Input 5
def Input5(channel):
    print "--> Input 5 aktiviert <--"
    print "Command: ", cmd_e
    os.system('bash -c "' + cmd_e + '"')

# Interrupts
GPIO.add_event_detect(in_a, edge_in_a, callback = Input1, bouncetime = bouncetime)
GPIO.add_event_detect(in_b, edge_in_b, callback = Input2, bouncetime = bouncetime)
GPIO.add_event_detect(in_c, edge_in_c, callback = Input3, bouncetime = bouncetime)
GPIO.add_event_detect(in_d, edge_in_d, callback = Input4, bouncetime = bouncetime)
GPIO.add_event_detect(in_e, edge_in_e, callback = Input5, bouncetime = bouncetime)
 
# Schleife (macht gar nichts, da GPIOs über Interrupts ausgelesen werden)
try:
    while True:
        time.sleep(1)
 
except:
  GPIO.cleanup()
  print "\nBye"
