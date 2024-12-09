from collections import deque
from Node import Node

def insert(root, value):
    if root is None:
        return Node(value)

    queue = deque([root])

    while queue:
        temp = queue.popleft()

        if temp.left is None:
            temp.left = Node(value)
            break
        else:
            queue.append(temp.left)

        if temp.right is None:
            temp.right = Node(value)
            break
        else:
            queue.append(temp.right)

    return root


def getMin(root):

    if root is None:
        return float('inf')

    res = root.value
    left_res = getMin(root.left)
    right_res = getMin(root.right)

    if left_res < res:
        res = left_res
    if right_res < res:
        res = right_res

    return res

def getMax(root):

    if root is None:
        return float('-inf')

    res = root.value
    left_res = getMax(root.left)
    right_res = getMax(root.right)

    if left_res > res:
        res = left_res
    if right_res > res:
        res = right_res

    return res


nums = [85, 70, 95, 60, 75, 90, 100]

root = Node(5)

for num in nums:
    root = insert(root, num)

print("Elementos após inserção ", end=" ")
print()
print("Minimo:", getMin(root))
print("Máximo:", getMax(root))
