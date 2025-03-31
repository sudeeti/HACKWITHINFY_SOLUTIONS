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

def sum_root_to_leaf(root, current_sum=0):
    if not root:
        return 0
    current_sum = current_sum * 10 + root.data
    if not root.left and not root.right:
        return current_sum
    return sum_root_to_leaf(root.left, current_sum) + sum_root_to_leaf(root.right, current_sum)

# Input handling
n = int(input())
arr = input().split()
root = insert_element(arr)
result = sum_root_to_leaf(root)
print(result)
