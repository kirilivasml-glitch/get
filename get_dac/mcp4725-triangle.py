import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 5.0
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = mcp.MCP4725(5.0, 0x61, True)

    t = 0.0
    while True:
        voltage = amplitude * sg.get_triangle_wave_amplitude(signal_frequency, t)
        dac.set_voltage(voltage)
        t += 1.0 / sampling_frequency
        sg.wait_for_sampling_period(sampling_frequency)
finally:
    dac.deinit()