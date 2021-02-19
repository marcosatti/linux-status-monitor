from serial import Serial
from cobs import cobs
from time import sleep
import struct

def run(port_path, reporting_period, status_callback):
    port = Serial(baudrate=115200)
    port.port = port_path
    port.dtr = True
    port.rts = True
    port.open()

    while (status := status_callback()) is not None:
        data = status.SerializeToString()
        checksum_value = checksum(data)
        encoded = cobs.encode(data)

        # Needs to be sent in one call otherwise the receiving device may think its different packets.
        port.write(struct.pack('B', 0x00) + struct.pack('<H', checksum_value) + encoded + struct.pack('B', 0x00))
        port.flush()

        sleep(reporting_period)

    port.close()

def checksum(data):
    value = 0
    for data_byte in data:
        value += int(data_byte)
    value = value % 0xFFFF
    return value
