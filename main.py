import driver
import status
import power
import network
import argparse
import sys
import traceback 
import signal

parser = argparse.ArgumentParser(description='Status reporter driver')
parser.add_argument('port', help='serial port that the reporter display device is connected to')
parser.add_argument('--period', type=float, default=1.0, help='the reporting period (default every second)')

args = parser.parse_args()

print('Start status monitor')

exit_code = -1

def sigint_handler(code, _frame):
    global exit_code
    exit_code = 0

signal.signal(signal.SIGINT, sigint_handler)

power.start(args.period)
network.start(args.period)

def status_callback():
    if exit_code >= 0:
        return None
    return status.get_status()

try:
    driver.run(args.port, args.period, status_callback)
except:
    traceback.print_exc()
    exit_code = 1

network.exit()
power.exit()

print('Exit status monitor')

sys.exit(exit_code)
