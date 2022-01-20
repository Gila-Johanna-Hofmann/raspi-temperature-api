# RaspberryPi Temperature Sensor API
A simple python program that reads data from a temperature sensor and makes it available via REST API

# Description
The program is part of a school assignment that emulates monitoring a server room for temperature. The assignment was to add a sensor to the Pi, read its output and make the data available. My study group used the DS1820 sensor to measure temperature via the Pi and put together a program that both reads from the sensor and publishes it via HTTPServer and REST API. We also added another Pi with a Node-Red module (that is not part of this project) that gets the measurements via the API and displays and stores them. This is all very simply done with no regards to security.

The DS1820 reads the temperature and puts it into a file in hex code. The file can be accessed on the Pi an the hex is converted into a string, the temperature-portion is used and converted to Celcius - a decimal with two digits. It is then put into JSON format, together with the current datetime (that was converted into JSON serializable format) and a ficticious name of the server room. An HTTPServer is set up on the Pi and upon a GET-call, a simple API provides the JSON. 

# Getting Started
## Dependencies
Python3

DS1820 temperature sensor (and any other stuff you need to cennect it to the Pi)
## Installing
Connect the sensor to your Pi --> a german how-to is added in the acknowledgements-section of the Readme.

Copy the python script to the Pi.

Add the ID of the temperature sensor to the script on top of the TemperatureReader-class --> instructions how to do so are also found in the same how-to.

Change the server port and "serverlocation" and/or add any additional info to the JSON if you want to.
## How to run the program
Run the program with Python3 --> the server should start.

You should be able to GET the JSON with the temperature via the Pi-IP and port in a browser, with Postman, Node-red or however you like.
## Help
A successful GET-request is printed to the console with the information the JSON-body will provide.

# Acknowledgments
Wolfgang Graab provides the instructions on how to connect the sensor to the Pi and the code to convert the sensor-output to Celcius.

[Wolfgang Graabs Website](https://webnist.de/kontakt/).

&

[@merlinschumacher](https://github.com/merlinschumacher) helped me with the server and API-portion of the code.
