import subprocess
from functools import reduce

def get_current_users_count():
    # Roughly equivalent...
    result = subprocess.run('smbstatus -p', shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        return 0
    iterable = filter(None, result.stdout.split('\n')[4:])
    return reduce(lambda s, e: s + 1, iterable, 0)

def get_open_files_count():
    # Roughly equivalent...
    result = subprocess.run('smbstatus -L', shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        return 0
    iterable = filter(None, result.stdout.split('\n')[3:])
    return reduce(lambda s, e: s + 1, iterable, 0)
