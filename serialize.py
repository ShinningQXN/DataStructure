# Serialize binary tree

# 【题目 297】：
# binary tree serialization

# 【算法】：
# dfs
# bfs

# 【dfs】：
# 1.in order，把遇到的value放进一个list里面，再把list变为str
# 2.用一个iter，讲list
class Code:
	def serilize(self, root):
		def pre_order(node):
			if node:
				vals.append(str(node.val))
				pre_order(node.left)
				pre_order(node.right)
			else:
				vals.append('#')
		vals = []
		pre_order(root)
		return ' '.join(vals)

	def deserilize(self, data):
		def helper():
			val = next(int(vals))
			if val == '#':
				return None
			else:
				node = TreeNode(val)
				node.left = helper()
				node.right = helper()
			return node
		vals = iter(data.split(' '))
		return helper()


# 【follow up 449】 
# 如果是BST呢？
# 如果是BST，就不用存null了，用bst的性质，来限制
# int max： sys.maxint int min: -sys.maxint - 1
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def buildString(node):
            if node:
                data.append(str(node.val))
                buildString(node.left)
                buildString(node.right)
        data = []
        buildString(root)
        return ' '.join(data)
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def buildTree(vals, vmin, vmax):
            if not vals:
                return None
            val = int(vals[0])
            if val < vmin or val > vmax:
                return None
            vals.popleft()
            node = TreeNode(val)
            node.left = buildTree(vals, vmin, val)
            node.right = buildTree(vals, val, vmax)
            return node
        if not data:
            return None
        vals = collections.deque(data.split(' ')) # cannot be ignore, deque(['']) exsit
        return buildTree(vals, -sys.maxint -1, sys.maxint)
    
