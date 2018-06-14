# 给两个char array，其中有一些char为backspace就是删除前面的字符，要求输出一个boolean判断两个char array是否相同，时间要求O(n) , 空间要求O(1)
# 例如：
# [a,b,'\b',d,c] 和[a,d,c] true
# [a,b,'\b','\b','\b',d,c] 和 [d,c] true
# [a,b,d,'\b'] 和 [a,d] false. 

# def isSame(arr1, arr2):
# 	i = 0
# 	count = 0
# 	for c in arr2:
# 		while i < len(arr1) and arr1[i] != c:
# 			i += 1
# 			if arr1[i] == '\b':
# 				count -= 1 if count > 0 else 0
# 			else:
# 				count += 1
# 		if i == len(arr1) and count > 0:
# 			return False
# 		i += 1
# 	while i < len(arr1):
# 		if arr1[i] == '\b':
# 			count -= 1 if count > 0 else 0
# 		else:
# 			count += 1
# 	return count == 0

def isSame(arr1, arr2):
	i, j = 0, 0
	count = 0
	while i < len(arr1):
		if i < len(arr1) and j < len(arr2) and arr1[i] == arr2[j]:
			i += 1
			j += 1
		elif arr1[i] == '\b':
			count -= 1 if count > 0 else 0
			i += 1
		else:
			count += 1
			i += 1
	return j == len(arr2) and count == 0

print isSame (['a', 'b', '\b', 'd', 'c'], ['a', 'd', 'c'])
print isSame (['a', 'b', '\b', '\b', '\b', 'd', 'c'], ['d', 'c'])
print isSame (['a', 'b', 'd', '\b'], ['a', 'd'])
print isSame (['a', 'b', 'd'], ['a', 'd'])
