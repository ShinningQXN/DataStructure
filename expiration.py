# 第二题地里出现过的带时间戳expiration的hashmap以及删除expired的entry. 

class Data(object):
	def __init__(self, key, value, expire_time):
		self.key = key
		self.value = value
		self.expire_time = expire_time
	def __le__()

class ExpiringMap():
	def __init__():
		self.map = {}
		self.heap = []

	def put(key, value, duration):
		self.clean_up()
		data = Data(key, value, duration + sys.get_now())
		heapq.heappush(heap, (data.expire_time, data))
		map[key] = data
	
	def get(key):
		self.clean_up()
		if key in map:
			return map[key]
		return None

	def clean_up():
		while len(heap) > 0 and heap[0][0] < sys.get_now():			
			data = heapq.heappop(heap)[1]
			del map[data.key]
