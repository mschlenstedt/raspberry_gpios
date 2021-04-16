# Raspberry GPIOs

Kleines Python-Skript, um die GPIOs desRaspberry als Inputs auszulesen und bei Betätigung beliebige Kommandos auszuführen. So ist es auch möglich, den Status der Eingänge per UDP an den Miniserver zu senden.

Das Skript "gpio_inputs.py" überwacht die GPIOs und führt bei Aktivierung die entsprechende Befehle in der Bash aus.

Das Skript "watchdog.sh" überwacht, ob "gpio_inputs.py" noch läuft und startet es gegebenenfalls neu. Es sollte per cron regelmäßig aufgerufen werden.

Alle Einstellungen werden am Anfang des Skripts "gpio_inputs.py" durchgeführt.

Die Eingänge können gegen Ground oder gegen +3.3V verschaltet werden.

Beschreibung des gesamten Projekts findet sich im Loxwiki: https://www.loxwiki.eu/x/MoVWBQ
