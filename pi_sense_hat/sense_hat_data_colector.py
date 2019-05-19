from datetime import datetime
from sense_hat import SenseHat
import json
from time import sleep

class PiSenseHat:

    def __init__(self):
        self.sense = SenseHat()  # define sensor object
        self.measurement = {
            "timestamp": 0,
            "temperature": 0,
            "pressure": 0,
            "humidity": 0,
            "acceleration": 0,
            "orientation": 0

        }

    @staticmethod
    def round_value(value):
        return round(value, 3)

    def round_values(self):
        for key, value in self.measurement.items():
            if key not in ["timestamp"]:
                if key in ["acceleration", "orientation"]:
                    for sub_key, sub_value in value.items():
                        self.measurement[key][sub_key] = self.round_value(sub_value)
                else:
                    self.measurement[key] = self.round_value(value)

    def get_measurement(self):
        self.measurement["timestamp"] = str(round(datetime.timestamp(datetime.now())*1000)) # rounded ms
        self.measurement["temperature"] = self.sense.get_temperature()
        self.measurement["pressure"] = self.sense.get_pressure()
        self.measurement["humidity"] = self.sense.get_humidity()
        self.measurement["orientation"] = self.sense.get_orientation()
        self.measurement["acceleration"] = self.sense.get_accelerometer_raw()

        self.round_values()

    def __repr__(self):

        return json.dumps(self.measurement, indent=4)


import requests

def post_to_web_page(IP: str, payload):
    resp = requests.post(IP, json=payload)
    if resp.status_code != 201:
        print(resp.status_code)

if __name__ == "__main__":

    IP = "http://phoebe.tano.si:8080/api/robot/senses"

    # todo add while loop
    while True:
    #for i in range(10):
        try:
            sleep(1)
            sensor = PiSenseHat()  # measure for one hour
            sensor.get_measurement()
            print(sensor)
            post_to_web_page(IP=IP, payload=sensor.measurement)
        except:
            sleep(1)

