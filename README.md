# ProjectDioclecian
Raspberry Pi garden assistant

<p>
  <img src="https://github.com/AR621/ProjectDioclecian/blob/main/showcase/garden.jpg?raw=true" height="350" />
  <img src="https://github.com/AR621/ProjectDioclecian/blob/main/showcase/pi.jpg?raw=true" height="350" />
</p>

## Description
This is a project I made that allows you to read data from several sensors on your raspberry pi (in my case raspberryPi zero) and then display it on a webserver hosted on Pi. Tou can host this server over the web and see how your garden is doing even when you are not home - which was the initial inspiration for this project.

## Techstack
- Sensors: Python3 - BME280 library
- Webserver: Python3 - Flask
- Webpage: HTML, CSS, javascript - chart.js

## Usage
The project should work out of the box on Raspberry Pi Zero assuming you connect it same way as I did, in case of other Pi's you will need to modify pin numbers in config.py
Once all is setup you can easly run the whole project by running dioclecian.py script which should initialize all other scripts by itself.

Command i suggest to run the project:
````
nohup python3 dioclecian.py &
````
That way you can easly have it run in the background evem when you log out of your Pi, it will also log it's standard console output to nohup.out which may be useful for debugging.


Feel free to use this project, modify it to your needs and write any suggestions.
## Webpage
Here is an screenshot showing how the webpage that displays the data looks:
![webpage example image](
https://github.com/AR621/ProjectDioclecian/blob/main/showcase/webpage_example.png?raw=true  "webpage example")
