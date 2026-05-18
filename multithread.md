▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄      
══════════════════════════════════════════    
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

▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄      
══════════════════════════════════════════      
fastAPI    
Using Gunicorn for production in Python (Flask/FastAPI) provides stability, concurrent request handling, and process management that development servers lack. Adding dedicated /healthz and /readyz endpoints ensures that orchestration tools like Kubernetes or Docker can monitor app liveness and traffic readiness.     
1. Implementation Example (FastAPI + Gunicorn)This approach adds endpoints that indicate whether the application is running (liveness) and ready to handle traffic (readiness), such as waiting for database connections   
3. Explanation of Endpoints    
/healthz (Liveness Probe): Tells orchestrators if the container is running. If this fails, the container is restarted. It should be lightweight, simply returning a 200 OK status.
/readyz (Readiness Probe): Tells orchestrators if the app is ready to accept traffic. It checks if external dependencies (databases, ML models, caches) are fully loaded. If it fails, the traffic is routed away, but the container is not restarted.     
```   
# main.py
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
import time

app = FastAPI()

# Simulation of a startup delay (e.g., waiting for database)
is_ready = False

@app.on_event("startup")
async def startup_event():
    global is_ready
    # Simulate DB connection check
    time.sleep(2)
    is_ready = True

# Liveness check: Is the process alive?
@app.get("/healthz")
async def liveness():
    return {"status": "ok", "message": "Alive"}

# Readiness check: Is the application ready to serve traffic?
@app.get("/readyz")
async def readiness():
    if is_ready:
        return {"status": "ok", "message": "Ready"}
    return JSONResponse(status_code=503, content={"status": "not_ready"})
````    
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄      
══════════════════════════════════════════      
Types of Creational Design Patterns in Python:    
Factory Method     
 Abstract Factory Method     
 Singleton Method    
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄      






















