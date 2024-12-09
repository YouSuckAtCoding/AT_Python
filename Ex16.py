from Node import Node

def get_successor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr


def insert(root, value):
    if root is None:
        return Node(value)

    if root.value == value:
        return root

    if root.value < value:
        root.right = insert(root.right, value)
    else:
        root.left = insert(root.left, value)
    return root


def deleteNode(root, x):
    
    if root is None:
        return root

    if root.value > x:
        root.left = deleteNode(root.left, x)
    elif root.value < x:
        root.right = deleteNode(root.right, x)

    else:
        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        succ = get_successor(root)
        root.value = succ.value
        root.right = deleteNode(root.right, succ.value)

    return root

def printTree(root):
    if root is None:
        return
    printTree(root.left)
    print(root.value, end=" ")
    printTree(root.right)

nums = [45,25,65,20,30,60,70]

root = Node(nums[0])

for i in range(1, len(nums) - 1):
    root = insert(root, nums[i])

print(printTree(root))
deleteNode(root, 20)
print(printTree(root))
deleteNode(root, 25)
print(printTree(root))
deleteNode(root, 45)
print(printTree(root))