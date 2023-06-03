import time
COUNT = 1000000000

def countdown(n, index):
    with open(f"countdown_{index}.txt", "w") as file:
        while n > 0:
            if n % 1000000 ==0:
                file.write(str(n) + "\n")
            n -= 1


start = time.time()
countdown(COUNT, -1)
end = time.time()

print('Time taken in seconds -', end - start)