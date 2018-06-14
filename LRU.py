# # 146. LRU Cache
# 【描述】
# LeetCode LRU
# 【算法】：
# 1.doublist + map
# 2.queue的操作分为remove, add to head, pop tail
# 3. map的操作就放在外面吧，不要放进queue的操作里面
# 【细节】：
# 1. next为python内置函数，用post代替next
# 2. node把key, value都存入？ 问面试官， 可以不存
# 3. self是def必须的，不然不过compiler
# 4. class doublist必须写在LRUclass外面
# 5. 调用自身时候别忘了self
# 6. 忘记return

class dnode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.post = None

class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.head = dnode(0,0)
        self.tail = dnode(0,0)
        self.mp = {}
        self.head.post = self.tail
        self.tail.pre = self.head
    
    def remove(self, node):
        pre = node.pre
        post = node.post
        pre.post = post
        post.pre = pre
        
    def add_to_head(self, node):
        node.post = self.head.post
        node.pre = self.head
        self.head.post = node
        node.post.pre = node
    
    def pop_tail(self):
        self.remove(self.tail.pre)
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.mp:
            return -1
        node = self.mp[key]
        self.remove(node)
        self.add_to_head(node)
   
        return node.value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.mp:
            node = dnode(key, value)
            self.mp[key] = node
            self.add_to_head(node)
            self.size += 1
            # print (self.tail.pre.value)
            
            if self.size > self.capacity:
                del self.mp[self.tail.pre.key]
                self.pop_tail()
                self.size -= 1

        else:
            node = self.mp[key]
            node.value = value
            self.remove(node)
            self.add_to_head(node)
        return node
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)