import random

def selectionSort(array):

    size = len(array)
    for i in range(size):
        min = i

        for j in range(i + 1, size):
            
            if array[j] < array[min]:
                min = j
        
        (array[i], array[min]) = (array[min], array[i])

scores = []
for x in range(0, 15):
    scores.append(random.randint(5, 60))

selectionSort(scores)
print(scores)

        
