import os
import signal
import time
import sys

def send_signal(pid, signal_num):
    try:
        os.kill(pid, signal_num)
        print(f"Sent signal {signal_num} to server")
    except ProcessLookupError:
        print("Server process not found.")

if len(sys.argv) < 2:
    print("Usage: python client.py <server_pid>")
    sys.exit(1)

server_pid = int(sys.argv[1])

while True:
    print("1. Send SIGUSR1")
    print("2. Send SIGUSR2")
    print("3. Quit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        send_signal(server_pid, signal.SIGUSR1)
    elif choice == '2':
        send_signal(server_pid, signal.SIGUSR2)
    elif choice == '3':
        print("Exiting client.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
