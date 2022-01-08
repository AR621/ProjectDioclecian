#!/usr/bin/python3

import time
import bme280 # handles air pressure and temperature sensor
import config as cfg
import csv
import RPi.GPIO as GPIO
import os

# Functions
def logData(datafile, time, data):
    dataPacket = [time, data]
    with open(datafile, 'a+',newline='') as openDataFile:
        writer = csv.writer(openDataFile)
        writer.writerow(dataPacket)
def readPin(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    return GPIO.input(pin)
#################################################################
# INIT 
print("Dioclecian initializing...")
(chip_id, chip_version) = bme280.readBME280ID()
print("Sensor", chip_id, "version", chip_version, "responsible fo temperature here, hi! :)")

#   First data
(tmp, prs, null) = bme280.readBME280All()
# Used as a countermeasure in case first data from sensor is garbled
# which was the case with my sensor

os.system("python3 " + cfg.SERVER_SCRIPT_NAME)
print("Dioclecian: server initialized")

#   SENSOR LOOP
while(1):
    # server check
    # Time trackers
    timeNow = time.strftime("%d.%m.%y %H:%M", time.localtime())  
    secondsNow = time.strftime("%S",time.localtime())
    minutesNow = time.strftime("%M",time.localtime())
    # Main measurment code
    if (secondsNow=="00"): # Every minute
        # pot humidity
        print(readPin(21))
        # temperature
        (tmp, prs, null) = bme280.readBME280All()
        print(timeNow,"; Temperature logged:", tmp)
        logData(cfg.TEMPERATURE, timeNow, tmp)
        if(minutesNow == "00" or minutesNow == "30"): # Every 30 minutes
            # pressure
            print(timeNow,"; Pressure logged:", prs)
            logData(cfg.PRESSURE, timeNow, prs)
    time.sleep(1)
exit(-1)



