import random

def binarysearch(array, selected):
    l = 0
    r = len(array) - 1

    it_count = 0
    while l < r:

        mid = (l + r) // 2

        if array[mid] == selected:
            print(it_count)
            return mid

        elif array[mid] > selected:
            r-=1
        else:
            l+=1

        it_count+=1

    return -1

def trashsearch(array, selected):

    it_count = 0

    for i in range(0, len(array) - 1):
        if array[i] == selected:
            print(it_count)
            return i
        it_count+=1

    return -1


random.seed(42)
isbns = sorted(random.randint(1000000000, 9999999999) for _ in range(100000))

selected = random.choice(isbns)
print(selected)
binarysearch(isbns, selected)
trashsearch(isbns, selected)

