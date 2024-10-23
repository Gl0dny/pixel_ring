from .apa102_pixel_ring import PixelRing

pixel_ring = PixelRing()

USAGE = '''
If the hardware is ReSpeaker 6 Mic Array for Pi
there is a power-enable pin which should be enabled at first.
:
    from gpiozero import LED
    power = LED(5)
    power.on()

'''

def main():
    import time

    print('Control APA102 RGB LEDs via SPI')
    print(USAGE)

    pixel_ring.think()
    time.sleep(3)
    pixel_ring.off()
    time.sleep(1)


if __name__ == '__main__':
    main()

