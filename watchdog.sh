#!/bin/bash

pgrep -f gpio_inputs.py >/dev/null 2>&1
if [[ $? -eq 1 ]]
then
  echo "Skript wird neu gestartet"
  ./gpio_inputs.py &
else
  echo "Skript läuft noch"
fi

