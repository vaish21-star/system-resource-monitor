import psutil
import platform
import time


def system_info():
    print("\n====== SYSTEM INFORMATION ======")
    print("Operating System:", platform.system())
    print("Release Version:", platform.release())
    print("Processor:", platform.processor())


def cpu_info():
    cpu_usage = psutil.cpu_percent(interval=1)
    print("\nCPU Usage:", cpu_usage, "%")

    if cpu_usage > 80:
        print("⚠ Warning: High CPU usage detected!")


def memory_info():
    memory = psutil.virtual_memory()
    print("\nMemory Usage:", memory.percent, "%")
    print("Total Memory:", round(memory.total / (1024**3), 2), "GB")
    print("Available Memory:", round(memory.available / (1024**3), 2), "GB")


def disk_info():
    disk = psutil.disk_usage('C:\\')
    print("\nDisk Usage:", disk.percent, "%")
    print("Total Disk Space:", round(disk.total / (1024**3), 2), "GB")
    print("Free Disk Space:", round(disk.free / (1024**3), 2), "GB")


def running_processes():
    print("\n====== Running Processes (Top 5 by Memory) ======")
    processes = []

    for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
        try:
            processes.append(proc.info)
        except:
            pass

    processes = sorted(processes, key=lambda x: x['memory_percent'], reverse=True)

    for process in processes[:5]:
        print(f"PID: {process['pid']}, Name: {process['name']}, Memory: {round(process['memory_percent'], 2)}%")


def main():
    system_info()
    cpu_info()
    memory_info()
    disk_info()
    running_processes()


if __name__ == "__main__":
    main()