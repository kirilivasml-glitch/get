import r2r_dac as r2r
import signal_generator as sg
import time

def get_triangle_wave_amplitude(freq, time):
    phase = (time * freq) % 1.0
    if phase < 0.5:
        return phase * 2
    return 2 - phase * 2

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.3, True)

    t = 0.0
    while True:
        voltage = amplitude * sg.get_triangle_wave_amplitude(signal_frequency, t)
        dac.set_voltage(voltage)
        t += 1.0 / sampling_frequency
        sg.wait_for_sampling_period(sampling_frequency)
finally:
    dac.deinit()