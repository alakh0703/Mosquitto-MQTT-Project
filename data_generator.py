import random
import time
import matplotlib.pyplot as plt
# Initializing the class with temperature range, fluctuation, and period

class TemperatureSensor:
    def __init__(self, temperature_range=(18, 21), fluctuation=3, period=60):
        self.temperature_range = temperature_range
        self.fluctuation = fluctuation
        self.period = period
        self.last_temperature = None
        self.last_time = None
        self.temperatures = []
        self.count = []

    # Method to generate random values
    def _generate_random_value(self):
        return random.uniform(0, 1)
    
    # Method to set the temperature range
    def set_temperature_range(self, base, delta):
        self.temperature_range = (base - delta, base + delta)
    
    # Method to set the fluctuation
    def set_fluctuation(self, base, delta):
        self.fluctuation = base + delta
    
    # Method to set the period
    def set_period(self, base, delta):
        self.period = int(base + delta)
    
    # Getting the temperature
    @property
    def temperature(self):
        current_time = time.time()
         # Check if last temperature reading was None or it has been greater than the period
        if self.last_temperature is None or current_time - self.last_time >= self.period:
            # Normalizing the value and getting the temperature
            normalized_value = self.get_normalized_value()
            temperature = (normalized_value * (self.temperature_range[1] - self.temperature_range[0])) + self.temperature_range[0]
            self.last_temperature = temperature
            self.last_time = current_time
            self.temperatures.append(temperature)
            self.count.append(len(self.temperatures))
        # If the last temperature reading was taken recently, return the last temperature
        else:
            temperature = self.last_temperature
        return temperature
    
    # Method to normalize the value
    def get_normalized_value(self):
        value = self._generate_random_value()
        value = value * self.fluctuation
        value = (value + self.fluctuation) / (2 * self.fluctuation)
        return value

    
id = 1

def create_data():
    global id
    sensor = TemperatureSensor()
    sensor.set_temperature_range(18, 3)
    sensor.set_fluctuation(1, 0.0001)
    sensor.set_period(10, 0)
    temp = sensor.temperature
    current_time = time.strftime("%H:%M:%S", time.localtime())
    time.sleep(2)
    data = {
        'Count': id ,
        'Time': current_time,
        'Temperature': temp,
    }
    id += 1
    return data

def print_data(data):
    print('Count:', data['Count'])
    print('Time:', data['Time'])
    print('Temperature:', data['Temperature'])


def create_data2(temperature_range, fluctuation, period):
    global id
    sensor = TemperatureSensor()
    sensor.set_temperature_range(temperature_range[0], temperature_range[1])
    sensor.set_fluctuation(fluctuation[0], fluctuation[1])
    sensor.set_period(period[0], period[1])
    temp = sensor.temperature
    current_time = time.strftime("%H:%M:%S", time.localtime())
    # time.sleep(2)
    data = {
        'Count': id ,
        'Time': current_time,
        'Temperature': temp,
    }
    id += 1
    return data
    

















    

# Creating an instance of the TemperatureSensor class

# sensor = TemperatureSensor()

# sensor.set_temperature_range(18, 3)

# sensor.set_fluctuation(1, 0.5)

# sensor.set_period(1, 1)

# print(sensor.temperature)

# for i in range(100):
#     temperature = sensor.temperature
#     print(f"Temperature reading {i+1}: {temperature}")
#     sensor.last_temperature = None
#     sensor.last_time = None


# plt.plot(sensor.count,sensor.temperatures)
# plt.xlabel('Count')
# plt.ylabel('Temperature')
# plt.show()


# plt.scatter(sensor.count,sensor.temperatures)
# plt.xlabel('Count')
# plt.ylabel('Temperature')
# plt.show()