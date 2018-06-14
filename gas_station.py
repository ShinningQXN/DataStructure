【题目】gas station
【算法】
1. dynamic max/min -> heap
2. 二分法， trial and error
【算法细节】
第一种，用heap的时候，用了很多pop和push，如果面试官说可以优化吗，这个时候可以直接用pop出来的和下一个栈顶以及最小值相比较，再放入，具体实现看version2 和version1的区别
第二种，用二分法，怎么试错？ 首先，start和end好确定，然后用mid和具体情况比较，如果最小最大区间的值为mid，则需要插入多少个加油站？用求出的值和K比较。
还有一个细节，对于有eps的，可以用start + e < end, start = mid, end = mid
【细节】
1.python3 1/2 = 0.5
2. heap 操作， python objst的比较函数


class Interval(object):
    def __init__(self, value, num):
        self.value = value
        self.num = num
    def __lt__(self, other):
        return self.value / self.num > other.value / other.num

class Solution:
	# version 1， n + k * lgn
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        heap = []
        
        for i in range(1, len(stations)):
            interval = Interval(stations[i] - stations[i -1], 1)
            heapq.heappush(heap, interval)
            
        while K > 0:
            top = heapq.heappop(heap)
            top.num += 1
            heapq.heappush(heap, top)
            K -= 1
        return heap[0].value / heap[0].num

    def minmaxGasDist(self, stations, K):
    	heap = []
    	for i in range(1, len(stations)):
            interval = Interval(stations[i] - stations[i -1], 1)
            heapq.heappush(heap, interval)
        threahold = (stations[-1] - stations[0]) / K
        while K > 0:
        	top = heapq.heappop(heap)
        	while K > 0 and (top.value / top.num > threahold or top.value / top.num > heap[0].value / heap[0].num):
        		top.num += 1
        		K -= 1
        	heapq.heapqpush(top)
        return heap[0].value / heap[0].num

    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        start, end = 0, (stations[-1] - stations[0]) / K
        while start + 1e-6< end:
            mid = start + (end - start) / 2
            count = 0
            for a, b in zip(stations, stations[1:]):
                count += math.ceil((b - a) / mid) - 1
            if count > K:
                start = mid
            else:
                end = mid
        return end

