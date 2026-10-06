import numpy
import time


def get_sin_wave_amplitude(freq, time):
    return (numpy.sin(2 * numpy.pi * freq * time) + 1) / 2


def wait_for_sampling_period(sampling_frequency):
    time.sleep(1.0 / sampling_frequency)


def get_triangle_wave_amplitude(freq, time):
    phase = (time * freq) % 1.0
    if phase < 0.5:
        return phase * 2
    return 2 - phase * 2