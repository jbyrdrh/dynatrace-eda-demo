#!/usr/bin/env python3

import multiprocessing
import time

def cpu_stress():
    while True:
        # Perform intensive calculations
        x = 0
        while True:
            x += 1
            if x > 1e6:
                x = 0  # Reset to avoid overflow

def run_stress_on_all_cores():
    num_cores = multiprocessing.cpu_count()
    print(f"Spawning {num_cores} processes to fully utilize the CPU")
    processes = []
    
    try:
        for _ in range(num_cores):
            p = multiprocessing.Process(target=cpu_stress)
            processes.append(p)
            p.start()

        # Keep the main process alive to allow CPU stress to continue
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("Process interrupted by user. Stopping all processes.")
        for p in processes:
            p.terminate()

if __name__ == "__main__":
    run_stress_on_all_cores()
