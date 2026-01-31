from machine import Pin, SoftI2C
from TEA5767 import Radio

i2c = SoftI2C(scl=Pin(1), sda=Pin(0), freq=400000)
radio = Radio(i2c)  # initialize and set to the lowest frequency
radio = Radio(i2c, freq=104.3)  # initialize and set to a specific frequency

print('Frequency: FM {}\nReady: {}\nStereo: {}\nADC level: {}'.format(
        radio.frequency, radio.is_ready,  radio.is_stereo, radio.signal_adc_level
        ))

'''
print("hello world")

radio = Radio(SoftI2C(scl=Pin(1), sda=Pin(0), freq=400000))

Radio.mute = True

Radio.change_freqency(radio,95.1)
'''