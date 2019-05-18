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
            "pitch": 0,
            "roll": 0,
            "yaw": 0,
            "x_acceleration": 0,
            "y_acceleration": 0,
            "z_acceleration": 0

        }

    @staticmethod
    def round_value(value):
        return round(value, 3)

    def round_values(self):
        for key, value in self.measurement.items():
            if key not in ["current_time"]:
                self.measurement[key] = self.round_value(value)

    def get_measurement(self):
        self.measurement["current_time"] = datetime.now()
        self.measurement["temperature"] = self.sense.get_temperature()
        self.measurement["pressure"] = self.sense.get_pressure()
        self.measurement["humidity"] = self.sense.get_humidity()
        orientation = self.sense.get_orientation()
        self.measurement["orientation"] = orientation
        self.measurement["pitch"] = orientation['pitch']
        self.measurement["roll"] = orientation['roll']
        self.measurement["yaw"] = orientation['yaw']
        acceleration = self.sense.get_accelerometer_raw()
        self.measurement["x_acceleration"] = acceleration['x']
        self.measurement["y_acceleration"] = acceleration['y']
        self.measurement["z_acceleration"] = acceleration['z']

        # self.round_values()

    def __repr__(self):

        return json.dumps(self.measurement, indent=4)

if __name__ == "__main__":

    for i in range(10):
        sleep(1)
        sensor = PiSenseHat()  # measure for one hour
        sensor.get_measurement()
        print(sensor)
