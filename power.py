import pyRAPL
from time import sleep
import threading

thread_handle = None
stop = False
wattage = 0

def thread_main(period):
    global wattage
    
    measure = pyRAPL.Measurement('global')

    while not stop:
        measure.begin()
        sleep(period)
        measure.end()
        rate = float(measure.result.pkg[0]) / period  # uW
        wattage = int(rate / 1e6)  # W

def start(period):
    global thread_handle
    global stop
    
    pyRAPL.setup() 

    stop = False
    thread_handle = threading.Thread(target=thread_main, args=(period,))
    thread_handle.start()

def exit():
    global thread_handle
    global stop

    stop = True
    thread_handle.join()
    thread_handle = None

def read_value():
    global thread_handle
    global wattage

    assert thread_handle is not None
    return wattage