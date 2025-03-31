lass BinaryTree:
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

def zigzag_traversal(root):
    if not root:
        return []
    result = []
    queue = [root]
    left_to_right = True
    while queue:
        level_size = len(queue)
        level_nodes = []
        for _ in range(level_size):
            node = queue.pop(0)
            level_nodes.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if not left_to_right:
            level_nodes.reverse()
        result.append(" ".join(map(str, level_nodes)))
        left_to_right = not left_to_right
    return "\n".join(result)

# Input handling
n = int(input())
arr = input().split()
root = insert_element(arr)
result = zigzag_traversal(root)
print(result)
