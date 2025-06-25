import time
import sys

while True:
    current_time = time.strftime("%I:%M:%S %p")
    sys.stdout.write("\rCurrent Time: " + current_time)
    sys.stdout.flush()
    
    time.sleep(1)
