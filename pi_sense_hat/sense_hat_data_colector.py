from datetime import datetime
from sense_hat import SenseHat
import json
from time import sleep

class PiSenseHat:

    def __init__(self):
        self.sense = SenseHat()  # define sensor object
        self.measurement = {
            "current_time": 0,
            "temperature": 0,
            "pressure": 0,
            "humidity": 0,
            "acceleration": 0,
            "orientation": 0

        }

    @staticmethod
    def round_value(value):
        # return round(value, 3)
        print(value)
        return value

    def round_values(self):
        for key, value in self.measurement.items():
            if key not in ["current_time"]:
                if key in ["acceleration", "orientation"]:
                    for sub_key, sub_value in value.items():
                        self.measurement[key][sub_key] = sub_value

                self.measurement[key] = self.round_value(value)

    def get_measurement(self):
        self.measurement["current_time"] = str(datetime.timestamp(datetime.now()))
        self.measurement["temperature"] = self.sense.get_temperature()
        self.measurement["pressure"] = self.sense.get_pressure()
        self.measurement["humidity"] = self.sense.get_humidity()
        self.measurement["orientation"] = self.sense.get_orientation()
        self.measurement["acceleration"] = self.sense.get_accelerometer_raw()

        self.round_values()

    def __repr__(self):

        return json.dumps(self.measurement, indent=4)

if __name__ == "__main__":

    for i in range(10):
        sleep(1)
        sensor = PiSenseHat()  # measure for one hour
        sensor.get_measurement()
        print(sensor)
