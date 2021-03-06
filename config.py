# THIS IS A CONFIG FILE
# allows u for easy configuration of things like names for csv files etc.

PATH="/home/pi/ProjectDioclecian/"

SENSOR_SCRIPT_NAME = "dioclecian.py"
SERVER_SCRIPT_NAME = "dioclecianServer.py"
LOG_NAME = "nohup.out"


# Humidity config
NUM_OF_POTS=5 # number of soil humidity sensors connected
DATA_CHANNELS = [21, 20, 16, 19, 26] # List containing GPIO corresponding do status from 
# soil humidity sensor ## MAKE SURE IT HAS SAME LENGTH AS THE VALUE OF NUM_OF_POTS!

# Chart settings TODO
SHORT_CHART = 1
LONG_CHART = 30

# data files names
PRESSURE="pressure_data.csv"
TEMPERATURE="temperature_data.csv"
