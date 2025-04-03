from picamera2 import PiCamera2
from picamera2.array import PiRGBArray
from sense_emu import SenseHat

sense = SenseHat()

while True:
    with PiCamera2() as camera:
        camera.resolution = (64, 64)
        with PiRGBArray(camera, size=(8, 8)) as stream:
            camera.capture(stream, format='rgb', resize=(8, 8))
            image = stream.array

    pixels = [
        pixel
        for row in image
        for pixel in row
    ]

    sense.set_pixels(pixels)