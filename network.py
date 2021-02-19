from time import sleep
import threading
import psutil

thread_handle = None
stop = False
network_usage = 0

def thread_main(period):
    global network_usage

    while not stop:
        net_stat_start = psutil.net_io_counters(pernic=False, nowrap=True)
        start_counter = net_stat_start.bytes_recv + net_stat_start.bytes_sent
        sleep(period)
        net_stat_end = psutil.net_io_counters(pernic=False, nowrap=True)
        end_counter = net_stat_end.bytes_recv + net_stat_end.bytes_sent
        rate = float(end_counter - start_counter) / period  # B/s
        network_usage = int((rate / 1024) / 1024)  # MiB/s

def start(period):
    global thread_handle
    global stop
    
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
    global network_usage

    assert thread_handle is not None
    return network_usage
