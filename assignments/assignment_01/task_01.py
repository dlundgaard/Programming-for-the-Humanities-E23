import sys
import time

"""
Indefinitely outputs left-aligned alternating wave to terminal until aborted.
Amplitude and period of wave adjustable through function arguments.
"""
def alternating_wave(peak_width = 9, period = 1):
    assert peak_width > 1
    try:
        current_width = 0
        rising = True
        while True:
            if current_width == peak_width:
                rising = False
            elif current_width == 0:
                rising = True
            current_width = current_width + 1 if rising else current_width - 1 # increment if currently rising, decrement otherwise
            if current_width:
                print("*" * current_width)
                time.sleep(1 / (peak_width * 2)) # scale to respect Hz unit for period
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    alternating_wave()