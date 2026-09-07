"""Thermosim - Thermostat Simulation Program"""

import random

# All Temperature in degrees Celsius

class Room:
    """Temperature and drift rate."""

    def __init__(self, indoor_temp, outdoor_temp, drift_rate):
        self.indoor_temp = indoor_temp
        self.outdoor_temp = outdoor_temp
        self.drift_rate = drift_rate

    def drift(self):
        """Temperature gain/loss due to outdoor temperature."""
        if self.indoor_temp > self.outdoor_temp:
            self.indoor_temp = round(self.indoor_temp - self.drift_rate, 2)

        elif self.indoor_temp < self.outdoor_temp:
            self.indoor_temp = round(self.indoor_temp + self.drift_rate, 2)

        else:
            drift = random.choice(True, False)

            if drift:
                self.indoor_temp += self.drift_rate
            else:
                self.indoor_temp -= self.drift_rate

class Thermostat:
    """Thermostat – decides whether the Heater or AC gets turned on."""

    def __init__(self, target, heating_threshold, cooling_threshold):
        self.target = target
        self.heating_threshold = heating_threshold
        self.cooling_threshold = cooling_threshold

    def decide(self):
        """Start – decided by heating / cooling threshold: 
           Stop – decided by equal or surpass target:"""

        if heater.is_on:
            # If reach target, turn off.
            if room.indoor_temp == self.target or room.indoor_temp > self.target:
                heater.is_on = False

                heater.turn_off()
                print("Heater OFF")

            # If not, keep heating.
            else:
                heater.heat()

        elif airConditioner.is_on:
            # If reach target, turn off.
            if room.indoor_temp == self.target or room.indoor_temp < self.target:
                airConditioner.is_on = False

                airConditioner.turn_off()
                print("AC OFF")

            # If not, keep cooling.
            else:
                airConditioner.cool()

        else:
            # Start heating if temp below threshold
            if room.indoor_temp < self.heating_threshold:
                self.use_heater()

            # Start cooling if temp above threshold
            elif room.indoor_temp > self.cooling_threshold:
                self.use_AC()

    def use_heater(self):
        print("Heater ON")
        heater.turn_on()
        heater.heat() # heat once

    def use_AC(self):
        print("AC ON")
        airConditioner.turn_on()
        airConditioner.cool() # cool once

class Heater:
    """Control heater action. Heats when turned on."""

    def __init__(self):
        self.heat_rate = 0.2
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def heat(self):
        if self.is_on:
            room.indoor_temp = round(self.heat_rate + room.indoor_temp, 2)

class AirConditioner:
    """Control AC action. Cools when turned on."""

    def __init__(self):
        self.cool_rate = -0.2
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def cool(self):
        if self.is_on:
            room.indoor_temp = round(self.cool_rate + room.indoor_temp, 2)

room = Room(40, 30, 0.05)
heater = Heater()
airConditioner = AirConditioner()
thermostat = Thermostat(25, 24, 26)

minute = 0
hour = 0

for i in range(120):
    """Main loop for HVAC control."""
    
    thermostat.decide()
    room.drift()
    
    print(f"{hour}:{minute} {room.indoor_temp}°C")
    
    minute += 1
    
    if minute == 60:
        hour += 1
        minute = 0