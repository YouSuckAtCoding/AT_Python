import random
import time

def bubbleSort(array):

    r = len(array) - 1

    for i in range(0, r):

        swapped = False

        for j in range(r, 0, -1):
            if array[j] < array[j -1]:
                array[j], array[j - 1] = array[j - 1], array[j]

            swapped = True

        if not swapped:
             break
random.seed(42)

firstlist = []
secondlist = []

for x in range(1000):
    firstlist.append(random.randint(0, 50000))

for x in range(10000):
    secondlist.append(random.randint(0, 50000))

start = time.time()
bubbleSort(firstlist)
end = time.time()

firstListResult = end - start

start = time.time()
bubbleSort(secondlist)
end = time.time()

secondListResult = end - start

print("Tempo de execução primeira lista:" ,firstListResult)
print("Tempo de execução second lista:", secondListResult)
print()
print(firstlist)
print(secondlist)

