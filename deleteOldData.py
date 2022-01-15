import pandas as pd
import csv
import os

def cleanData(datafile):
    os.rename(datafile,"TEMP" + datafile)
    with open("TEMP" + datafile, mode ='r') as file:
        data = csv.reader(file, delimiter=',')
        dataList = list()
        for line in data:
            dataList.append(line)
        dataList = dataList[-1440*60:] # By default keeps 60 days of data
        with open(datafile, 'a+', newline='') as newFile:
                writer = csv.writer(newFile)
                for line in dataList:
                    writer.writerow(line)
    os.remove("TEMP" + datafile)

