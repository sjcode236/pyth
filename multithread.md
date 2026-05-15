
multiprocessing and multithreading:-    
In Python, the choice between multiprocessing and multithreading depends on whether your task is "waiting" for something else or doing heavy "thinking."    
- Multithreading is for I/O-bound tasks (waiting for network, disk, or user input). It lets multiple tasks appear to run at once while sharing the same memory.    
- Multiprocessing is for CPU-bound tasks (heavy calculations). It bypasses Python's Global Interpreter Lock (GIL) by giving each task its own CPU core and memory space     














