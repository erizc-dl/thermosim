"""Thermosim - Thermostat Simulation Program"""

# unit - celcius
indoor_temp = 20

cool_rate = -0.2
heat_rate = 0.2

target_temp = 120

sim_time = 1440 # set sim time (min)

min = 0
hour = 0

def airConditioner(temp):
    temp += cool_rate
    return temp

def heater(temp):
    temp += heat_rate
    return temp

def thermostat(temp, target):
    if temp > target:
        return airConditioner(temp)
    elif temp < target:
        return heater(temp)
    else:
        return None

for i in range(sim_time):
    print(f"{hour}:{min} - {indoor_temp} °C")

    if thermostat(indoor_temp, target_temp) is None:
        print(f"{hour}:{min} - *thermostat off")
        break

    new_temp = thermostat(indoor_temp, target_temp)
    indoor_temp = round(new_temp, 2)

    min += 1

    if min == 60:
        hour += 1
        min = 0