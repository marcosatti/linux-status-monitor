# Linux Status Monitor
## For home servers running Samba

Collects statistics into a message in order to be displayed.

Intended to be used with the stm32-status-monitor project.

Requirements:
- Running Linux
- Running on an Intel CPU (uses Intel RAPL - maybe it works on AMD/other?).
- Python (+ dependencies, see `requirements.txt`)

Systemd unit file included for automatic start up. 
