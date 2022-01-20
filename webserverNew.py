#import all needed libraries: HTTPServer, JSON, DateTime, os/sys/time for Raspi hardware and Math
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import datetime
import os, sys, time
import math


#define a port for the HTTPServer-API
serverPort = 8080


#turn datetime into JSON serializable format because it won't on itself fml
class DateTimeEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, datetime.datetime):
            return (str(z))
        else:
            return super().default(z)


#reads temperature from Raspi
class TemperatureReader:
    def readTemperature(self):
        # read wire slave file via ID of used temperature sensor - add the ID before the file name
        file = open('/sys/bus/w1/devices/28-03199779208f/w1_slave')
        filecontent = file.read()
        file.close()

        # read temperature measurements and convert them into desired format
        stringvalue = filecontent.split("\n")[1].split(" ")[9]
        temperature = float(stringvalue[2:]) / 1000

        # return formatted measurements
        return(round(temperature,2))
    
    def printTemp(self):
        print(stringvalue)


#manages all needed information and serializes it to JSON format
class Management:
    #initialize all needed variables
    def __init__(self) -> None:
        # ficticous location for the server
        self.serverlocation = "Raum1"
        # datetime of the measurement
        self.datetime = datetime.datetime.now()
        # the actual temperature measurement from the TemperatureReader-class
        self.temperatureReader = TemperatureReader()

    # reads the initialized variables and serializes the information into JSON format
    #note: "cls" looks at every JSON element and checks if it's a datetime to convert
    def __call__(self) -> str:
        return json.dumps({"temperature": self.temperatureReader.readTemperature(), "datetime": self.datetime, "location": self.serverlocation}, cls=DateTimeEncoder)


# initialize Management instance to use with HTTPServer
datamanagement = Management()


# the webserver itself with only a GET-function
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # default response
        self.send_response(200)

        # datamanagement calls itself because of "call"-funnction, no other function needed
        response = datamanagement()
        # print to console for debugging
        print("You'll get this response: " + response)
        
        # information about the message-header
        self.send_header("Content-type", "application/json")  
        # end of header
        self.end_headers()
        # answer to client, contains body of JSON (because response = Management = returns JSON)
        self.wfile.write(bytes(response, 'utf-8'))

    
# runs the webserver on default IP 0.0.0.0 and port 8080
if __name__ == "__main__":        
    webServer = HTTPServer(("0.0.0.0", serverPort), RequestHandler)
    print("Server started http://0.0.0.0:%s" % (serverPort))
    webServer.serve_forever()




