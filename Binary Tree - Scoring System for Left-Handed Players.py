class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def insert_element(arr):
    if not arr:
        return None
    root = BinaryTree(int(arr[0]))
    queue = [root]
    i = 1
    while i < len(arr):
        curr = queue.pop(0)
        if curr:
            if arr[i] != "null":
                curr.left = BinaryTree(int(arr[i]))
                queue.append(curr.left)
            i += 1
            if i < len(arr) and arr[i] != "null":
                curr.right = BinaryTree(int(arr[i]))
                queue.append(curr.right)
            i += 1
    return root

def sum_left_leaves(root):
    if not root:
        return 0
    total = 0
    if root.left and not root.left.left and not root.left.right:
        total += root.left.data
    total += sum_left_leaves(root.left)
    total += sum_left_leaves(root.right)
    return total

# Input handling
n = int(input())
arr = input().split()
root = insert_element(arr)
result = sum_left_leaves(root)
print(result)
