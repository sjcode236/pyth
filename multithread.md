
multiprocessing and multithreading:-    
In Python, the choice between multiprocessing and multithreading depends on whether your task is "waiting" for something else or doing heavy "thinking."    
- Multithreading is for I/O-bound tasks (waiting for network, disk, or user input). It lets multiple tasks appear to run at once while sharing the same memory.    
- Multiprocessing is for CPU-bound tasks (heavy calculations). It bypasses Python's Global Interpreter Lock (GIL) by giving each task its own CPU core and memory space   
Multithreading allows multiple tasks to run within a single process. Because Python’s Global Interpreter Lock (GIL) only allows one thread to execute Python code at a time.  Multiprocessing creates separate instances of the Python interpreter, each with its own memory and its own GIL. This allows tasks to run in parallel across multiple CPU cores. Multithreading: This refers to the ability of a processor to execute multiple threads concurrently, where each thread runs a process.
Multiprocessing: This refers to the ability of a system to run multiple processors in parallel, where each processor can run one or more threads.     

Receiver Example: Multithreading vs. Multiprocessing  
1. Multithreading Example (The "I/O Receiver"):-  Best for when your receiver spends most of its time waiting for incoming network packets.    
```
import threading
import time

def data_receiver(name):
    print(f"Receiver {name} started...")
    # Simulate waiting for network data
    time.sleep(2) 
    print(f"Receiver {name} finished receiving data.")

# Threads share memory, making it easy to pass data back to the main app
threads = []
for i in range(3):
    t = threading.Thread(target=data_receiver, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```
2. Multiprocessing Example (The "Parallel Receiver"):-
Best if your receiver has to perform complex decryption or heavy data parsing on every incoming message.
```
import multiprocessing
import os

def heavy_receiver(name):
    print(f"Receiver {name} (Process ID: {os.getpid()}) starting computation...")
    # Simulate heavy CPU work (e.g., complex calculations)
    sum(i * i for i in range(10**7))
    print(f"Receiver {name} finished processing.")

if __name__ == "__main__":
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=heavy_receiver, args=(f"Process-{i}",))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
```

















