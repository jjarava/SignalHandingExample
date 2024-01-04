import os
import signal
import time

info=""

def sigusr1_handler(signum, frame):
    print("Server received SIGUSR1 signal")
    print(" -- Adding a 0 to the array")
    global info
    info += "0"
    print("Array so far, ", info)

def sigusr2_handler(signum, frame):
    print("Server received SIGUSR2 signal")
    print(" -- Adding a 1 to the array")                                                                                                                      
    global info                                                                                                                                               
    info += "1"                                                                                                                                               
    print("Array so far, ", info)                                                                                                                             

# Register signal handlers
signal.signal(signal.SIGUSR1, sigusr1_handler)
signal.signal(signal.SIGUSR2, sigusr2_handler)

# Print the server's PID
print(f"Server PID: {os.getpid()}")

print("Server is running...")

while True:
    time.sleep(1)
