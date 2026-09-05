"""Thermosim - Thermostat Simulation Program"""

# unit - celcius
indoor_temp = 30
outdoor_temp = 40

cool_rate = -0.2
heat_rate = 0.2
drift_rate = 0.05

target_temp = 25

sim_time = 1440 # set sim time (min)

min = 0
hour = 0

def airConditioner(temp):
    temp += cool_rate
    return temp

def heater(temp):
    temp += heat_rate
    return temp

def drift(temp):
    if temp > outdoor_temp:
        temp -= drift_rate
        return temp
    elif temp < outdoor_temp:
        temp += drift_rate
        return temp
    else:
        return temp # no drift

def thermostat(temp, target):
    if temp > target:
        return airConditioner(temp)
    elif temp < target:
        return heater(temp)
    else:
        return temp

for i in range(sim_time):
    print(f"{hour}:{min} - {indoor_temp} °C")

    if thermostat(indoor_temp, target_temp) == indoor_temp:
        print(f"{hour}:{min} - *thermostat off")

    new_temp = thermostat(indoor_temp, target_temp)
    new_temp = drift(new_temp)
    indoor_temp = round(new_temp, 2)

    min += 1

    if min == 60:
        hour += 1
        min = 0
