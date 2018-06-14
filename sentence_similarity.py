# sentence_similarity

方法一：
unionfind
用的是hashmap版本的unionfind，操作一次的时间复杂度为lgn


class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        def find(x):
        	# init
            if x not in map:
                map[x] = x
                return x
            # find the big boss
            f = x
            while map[f] != f:
                f = map[f]
            
            # give big boss to each node in the path
            while x != f:
                tmp = map[x]
                map[x] = f
                x = tmp
            return f
                
                    
        if len(words1) != len(words2):
            return False
        
        map = {}
        for p1, p2 in pairs:
            f1 = find(p1)
            f2 = find(p2)
            if f1 != f2:
                map[f1] = f2
        print (map)
        for w1, w2 in zip(words1, words2):
            if w1 != w2 and find(w1) != find(w2):
                # print(w1, w2)
                return False
        return True

方法二：dfs，用dfs的方法将每个词都贡献一个root