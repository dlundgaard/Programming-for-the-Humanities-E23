import sys
import time

"""
Indefinitely outputs left-aligned alternating wave to terminal.
Amplitude (and thus period width/duration) of wave adjustable through function arguments.
Number of periods run before terminating can be specified, otherwise indefinite or until keyboard interrupt.
"""
def alternating_wave(peak_width = 9, cycles = None):
    assert peak_width > 1
    assert cycles > 0

    current_width = 0
    rising = True
    cycle_index = 0

    try:
        while True:
            if current_width == peak_width:
                rising = False
            elif current_width == 0:
                rising = True
                cycle_index += 1

            current_width = current_width + 1 if rising else current_width - 1

            if cycles and cycle_index > cycles:
                break

            if current_width:
                print("*" * current_width)
                time.sleep(1 / (peak_width * 2)) # scale to respect Hz unit for period
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    alternating_wave(cycles = 2)