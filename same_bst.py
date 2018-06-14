class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

Solution1
def fun(p1, p2):
    def inorder(root, s):
        if root == None:
            return
        inorder(root.left, s)
        s.append(root.val)
        inorder(root.right, s)
    s1 = []
    s2 = []
    inorder(p1, s1)
    inorder(p2, s2)
    return "".join(str(s1)) == "".join(str(s2))

Solution2:
def fun(p1, p2):
    iter1 = (p1)
    iter2 = (p2)
    while iter1.hasNext() and iter2.hasNext():
        if iter1.next() == iter2.next():
            continue
        else:
            return False
    return !iter1.hasNext() and !iter2.hasNext()
a1 = TreeNode(1)
a2 = TreeNode (2)
a3 = TreeNode (3)
a2.left = a1
a2.right = a3

b1 = TreeNode (1)
b2 = TreeNode (2)
b3 = TreeNode (3)
b4 = TreeNode(4)

b1.right = b2
b2.right = b3
b3.right = b4

print (fun(a2, b1))

while t1.hasnext() and t2.hasnext():
    if t1.next() == t2.next():
        continue
    else:
        return False

return !t1.hasnext() and !t2.hasnext()








