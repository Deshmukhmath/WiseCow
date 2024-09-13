import psutil
import logging
import time

# Set logging configuration
logging.basicConfig(filename='system_health.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define threshold values
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage
PROCESS_THRESHOLD = 300  # Number of processes

def check_cpu_usage():
    """Checks CPU usage and logs if it exceeds the threshold."""
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
    return cpu_usage

def check_memory_usage():
    """Checks memory usage and logs if it exceeds the threshold."""
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High memory usage detected: {memory_usage}%")
    return memory_usage

def check_disk_space():
    """Checks disk usage and logs if it exceeds the threshold."""
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"Low disk space: {disk_usage}% used")
    return disk_usage

def check_running_processes():
    """Checks number of running processes and logs if it exceeds the threshold."""
    process_count = len(psutil.pids())
    if process_count > PROCESS_THRESHOLD:
        logging.warning(f"High number of running processes: {process_count}")
    return process_count

def monitor_system_health():
    """Monitors the system's health and logs alerts when thresholds are exceeded."""
    while True:
        cpu = check_cpu_usage()
        memory = check_memory_usage()
        disk = check_disk_space()
        processes = check_running_processes()

        logging.info(f"CPU usage: {cpu}%, Memory usage: {memory}%, Disk usage: {disk}%, Running processes: {processes}")

        # Check every 60 seconds
        time.sleep(60)

if __name__ == "__main__":
    monitor_system_health()
