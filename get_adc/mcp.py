import time
import adc_plot
import mcp3021_driver

adc = mcp3021_driver.MCP3021(5.0)

voltage_values = []
time_values = []
duration = 3.0

try:
    start_time = time.time()

    while (time.time() - start_time) <= duration:
        voltage_values.append(adc.get_voltage())
        time_values.append(time.time() - start_time)

    adc_plot.plot_voltage_vs_time(time_values, voltage_values, 5.0)
    adc_plot.plot_sampling_period_hist(time_values)
finally:
    adc.deinit()