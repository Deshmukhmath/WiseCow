### How the script works:

**psutil**: The script uses the psutil library to gather system statistics like CPU usage, memory usage, disk space, and the number of running processes.

**Thresholds**: The script checks if these statistics exceed predefined thresholds:
CPU usage > 80%
Memory usage > 80%
Disk space usage > 80%
Number of running processes > 300

**Logging**: If any of these thresholds are exceeded, the script logs a warning message to the system_health.log file.
Monitor loop: The system health is checked every 60 seconds.
