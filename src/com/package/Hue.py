#!/usr/bin/python

from phue import Bridge

b = Bridge('192.168.0.187')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
b.get_api()


lights = b.lights

# Print light names
for l in lights:
    print(l.name)
    print(l.brightness)
    
# Get a dictionary with the light id as the key
lights = b.get_light_objects('id')
print(lights)

# Get the name of light 1, set the brightness to 127
lights[1].name
lights[1].brightness = 127

# Get the name of light 2, set the brightness to 127
lights[2].name
lights[2].brightness = 127