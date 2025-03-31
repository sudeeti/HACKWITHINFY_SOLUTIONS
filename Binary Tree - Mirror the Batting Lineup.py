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

def mirror_tree(root):
    if not root:
        return None
    root.left, root.right = mirror_tree(root.right), mirror_tree(root.left)
    return root

def level_order_traversal(root):
    if not root:
        return ""
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        result.append(str(node.data))
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return " ".join(result)

# Input handling
n = int(input())
arr = input().split()
root = insert_element(arr)
root = mirror_tree(root)
result = level_order_traversal(root)
print(result)
