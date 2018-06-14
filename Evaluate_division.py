# Leetcode 399
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        pairs = {}
        result = []
        for i in range (len (equations)):
            if equations[i][0] not in pairs:
                pairs[equations[i][0]] = []
            if equations[i][1] not in pairs:
                pairs[equations[i][1]] = []
            pairs[equations[i][0]].append ([equations[i][1], values[i]])
            pairs[equations[i][1]].append ([equations[i][0], 1.0 / values[i]])
        print pairs
        for query in queries:
            change = self.bfs (pairs, query[0], query[1])
            result.append (change)
        return result

    def bfs(self, pairs, start, end):
        if start not in pairs or end not in pairs:
            return -1.0
        if start == end:
            return 1.0
        queue = collections.deque()
        queue.append([start, 1.0])
        visited = set()
        visited.add(start)
        while len(queue) > 0:
            curr = queue.popleft()
            for nei in pairs[curr[0]]:
                if nei[0] not in visited:
                    if nei[0] == end:
                        return curr[1] * nei[1]
                    queue.append([nei[0], curr[1] * nei[1]])
                    visited.add(nei[0])
        return -1.0

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        pairs = {}
        result = []
        for i in range (len (equations)):
            if equations[i][0] not in pairs:
                pairs[equations[i][0]] = []
            if equations[i][1] not in pairs:
                pairs[equations[i][1]] = []
            pairs[equations[i][0]].append ([equations[i][1], values[i]])
            pairs[equations[i][1]].append ([equations[i][0], 1.0 / values[i]])
        print pairs
        for query in queries:
            change = self.dfs (pairs, query[0], query[1], set ())
            result.append (change)
        return result

    def dfs(self, pairs, start, end, visited):
        if start not in pairs or end not in pairs or start in visited:
            return -1.0
        if start == end:
            return 1.0
        visited.add(start)
        for neighbor in pairs[start]:
            value = 1.0
            if neighbor[0] not in visited:
                value *= self.dfs (pairs, neighbor[0], end, visited) * neighbor[1]
                if value > 0:
                    return value
        return -1.0
                