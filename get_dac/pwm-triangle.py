import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = pwm.PWM_DAC(12, 500, 3.25, True)

    t = 0.0
    while True:
        voltage = amplitude * sg.get_triangle_wave_amplitude(signal_frequency, t)
        dac.set_voltage(voltage)
        t += 1.0 / sampling_frequency
        sg.wait_for_sampling_period(sampling_frequency)
finally:
    dac.deinit()