import time
import multiprocessing

COUNT = 1000000000

def countdown(n, index):
    with open(f"countdown_{index}.txt", "w") as file:
        while n > 0:
            if n % 1000000 == 0:
                file.write(str(n) + "\n")
            n -= 1

if __name__ == '__main__':
    num_processes = 100
    max_processes_at_a_time = multiprocessing.cpu_count()

    start = time.time()

    with multiprocessing.Pool(processes=max_processes_at_a_time) as pool:
        for i in range(num_processes):
            pool.apply_async(countdown, args=(COUNT // num_processes, i))

        pool.close()
        pool.join()

    end = time.time()

    print('Time taken in seconds -', end - start)
