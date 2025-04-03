import time
from sense_emu import SenseHat

sense = SenseHat()
sense.clear(255, 127, 0)

print(sense.gamma)
time.sleep(2)

sense.gamma = list(reversed(sense.gamma))
print(sense.gamma)
time.sleep(2)

sense.low_light = True
print(sense.gamma)
time.sleep(2)

sense.low_light = False
sense.gamma_reset()