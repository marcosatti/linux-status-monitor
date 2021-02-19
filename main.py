import driver
import status
import power
import network
import argparse
import sys
import traceback 

parser = argparse.ArgumentParser(description='Status reporter driver')
parser.add_argument('port', help='serial port that the reporter display device is connected to')
parser.add_argument('--period', type=float, default=1.0, help='the reporting period (default every second)')

args = parser.parse_args()

print('Start status monitor')

power.start(args.period)
network.start(args.period)

try:
    driver.run(args.port, args.period, status.get_status)
except:
    traceback.print_exc()

network.exit()
power.exit()

print('Exit status monitor')
