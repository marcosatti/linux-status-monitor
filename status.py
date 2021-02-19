from status_pb2 import Status
import power
import psutil
import cputemp.cputemp as cputemp
import network
import samba

def get_status():
    status = Status()
    status.cpu = int(psutil.cpu_percent())
    status.cpu_power = power.read_value()
    status.temperature = int(cputemp.readTemp() / 1000)
    status.network = network.read_value()
    status.samba_users_connected = samba.get_current_users_count()
    status.samba_files_opened = samba.get_open_files_count()
    return status
