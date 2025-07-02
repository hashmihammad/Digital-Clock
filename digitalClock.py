import time
import sys

while True:
    current_time = time.strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
    sys.stdout.write("\r" + current_time)
    sys.stdout.flush()
    time.sleep(1)
