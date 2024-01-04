## Basic Signal handling example

To run this example, follow these steps:
1. Start the server in one terminal: `python server.py`  
2. Get the server's process ID (PID).  The server process will print the PID when launched
3. Start the client in another terminal: `python client.py <server_pid>` where `<server_pid>` is the PID of the server process.  

The client can send SIGUSR1 or SIGUSR2 signals to the server, and the server will respond accordingly.
Please note that this is a basic example, and in a real-world scenario, you would likely implement more robust error handling and message passing logic.

The signal handlers have logic to add information to a global array depending on what signal is received.
