from flask import Flask, render_template
import pandas as pd
import csv
import config as cfg

dPressure = pd.read_csv("~/Dioclecian/Pressure.csv")
# Functionw
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
    DATA_PATH="/home/pi/Dioclecian/"

    labelsP = loadData(cfg.PATH + cfg.PRESSURE,0,0)
    valuesP = loadData(cfg.PATH + cfg.PRESSURE,1,1)

    labelsT = loadData(cfg.PATH + cfg.TEMPERATURE,0,0)
    valuesT = loadData(cfg.PATH + cfg.TEMPERATURE,1,1)

    return render_template("index.html", labelsP=labelsP, valuesP=valuesP, labelsT=labelsT, valuesT=valuesT, labelsT24=labelsT[-1440*cfg.SHORT_CHART:], valuesT24=valuesT[-1440*cfg.SHORT_CHART:])

@app.route('/jd')
def jd():
    return "JD!"

# Run the server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

