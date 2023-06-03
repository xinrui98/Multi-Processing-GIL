import time
import multiprocessing
from config import COUNT, NUM_PROCESSES

def countdown(n, index):
    with open(f"countdown_{index}.txt", "w") as file:
        while n > 0:
            if n % 1000000 == 0:
                file.write(str(n) + "\n")
            n -= 1

if __name__ == '__main__':
    max_processes_at_a_time = multiprocessing.cpu_count()

    start = time.time()

    with multiprocessing.Pool(processes=max_processes_at_a_time) as pool:
        for i in range(NUM_PROCESSES):
            pool.apply_async(countdown, args=(COUNT // NUM_PROCESSES, i))

        pool.close()
        pool.join()

    end = time.time()

    print('Time taken in seconds -', end - start)
