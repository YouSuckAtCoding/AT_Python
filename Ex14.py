from Node import Node

def insert(root, key):
    if root is None:
        return Node(key)

    if root.value == key:
        return root

    if root.value < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root


def search(root, value):

    if root is None or root.value == value:
        return root

    elif value > root.value:
        return search(root.right, value)
    else:
        return search(root.left, value)


def printTree(root):
    if root is None:
        return
    printTree(root.left)
    print(root.value, end=" ")
    printTree(root.right)


nums = [100, 50, 150, 30, 70, 130, 170]

root = Node(nums[0])

for i in range(1, len(nums) - 1):
    root = insert(root, nums[i])

print("Elementos em ordem", end=" ")
printTree(root)
print()
print("Disponível" if search(root, 70) else "Indisponível")
