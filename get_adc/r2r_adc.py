import RPi.GPIO as GPIO
import time


class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def number_to_dac(self, number):
        bits = [int(element) for element in bin(number)[2:].zfill(8)]
        GPIO.output(self.bits_gpio, bits)

    def sequential_counting_adc(self):
        for number in range(256):
            self.number_to_dac(number)
            time.sleep(self.compare_time)

            if GPIO.input(self.comp_gpio) == 0:
                if self.verbose:
                    print(f"Код АЦП: {number}")
                return number

        if self.verbose:
            print("Код АЦП: 255")
        return 255

    def get_sc_voltage(self):
        number = self.sequential_counting_adc()
        voltage = (number / 255.0) * self.dynamic_range
        return voltage

    def  successive_approximation_adc(self):
        result = 0
        bits = [128, 64, 32, 16, 8, 4, 2, 1]

        for bit in bits:
            test_value = result + bits
            self.number_to_dac(test_value)

            if GPIO.input(self.comp_gpio) == 1:
                result = test_value

        if self.verbose:
            print(f"Код АЦП (SAR): {result}")

        return result

    def get_sar_voltage(self):
        number  = self.successive_approximation_adc()
        voltage = (number /255.0) * self.dynamic_range

        return voltage


if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.3)

        while True:
            voltage = adc.get_sar_voltage()
            print(f"Напряжение: {voltage:.3f} В")

    except KeyboardInterrupt:
        pass

    finally:
        adc.deinit()