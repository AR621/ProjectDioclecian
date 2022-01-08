from flask import Flask, render_template
import pandas as pd
import csv
import config as cfg
import readPin as pin # handles reading pin status

# Functions
def loadData(datafile, returnCol=0, numeric=False):
    with open(datafile, mode ='r')as file:
        data = csv.reader(file, delimiter=',')
        dataOut=list()
        for line in data:
            if(numeric==True):
                line[returnCol]=round(float(line[returnCol]),2)
            dataOut.append(line[returnCol])
        return dataOut

app = Flask(__name__)


# webserver routes
@app.route('/')
def index():
    # Presssure data
    labelsP = loadData(cfg.PATH + cfg.PRESSURE,0,0)
    valuesP = loadData(cfg.PATH + cfg.PRESSURE,1,1)
    # Temperature data
    labelsT = loadData(cfg.PATH + cfg.TEMPERATURE,0,0)
    valuesT = loadData(cfg.PATH + cfg.TEMPERATURE,1,1)
    #pin data
    potInfoString = "" # displays nothing when no pots are configured in config.py
    potCount = 1
    for datapin in cfg.DATA_CHANNELS:
        if (pin.readPin(datapin)):
            potInfoString = potInfoString + "pot " + str(potCount) + " needs watering!\n"            
        else:
            potInfoString = potInfoString + "pot " + str(potCount) + " has water.\n"            
            potCount+=1

    return render_template("index.html", labelsP=labelsP, valuesP=valuesP, labelsT=labelsT, valuesT=valuesT, labelsT24=labelsT[-1440*cfg.SHORT_CHART:], valuesT24=valuesT[-1440*cfg.SHORT_CHART:], potInfo=potInfoString)

# Run the server
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

