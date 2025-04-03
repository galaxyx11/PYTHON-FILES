# This file displays tempature bars


from sense_emu import SenseHat

sense = SenseHat()

red = (255, 124, 0)
blue = (0, 125, 255)

while True:
    temp = sense.temp
    pixels = [red if i < temp else blue for i in range(64)]
    sense.set_pixels(pixels)
