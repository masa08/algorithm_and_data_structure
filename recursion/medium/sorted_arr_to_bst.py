class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def sortedArrToBST(numberList):
    if not numberList: return None
    pivod = getPivot(numberList)
    node = BinaryTree(numberList[pivod])
    node.left = sortedArrToBST(numberList[:pivod])
    node.right = sortedArrToBST(numberList[pivod+1:])
    return node

def getPivot(arr):
    if len(arr) % 2 == 0: return len(arr) // 2 - 1
    else: return len(arr) // 2
