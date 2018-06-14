max chunks to make sorted

769
不要一开始就想全部写出来，从test case开始写起来

01234
10234
30124

curr max < all right

def max_chunks(arr):
	n = len(arr)
	mem = [0 for i in range(n)]
	curr = n
	for i in range(n - 1, -1, -1):
		curr = min(curr, arr[i])
		mem[i] = curr

	curr = 0
	count = 1
	for i in range(n - 1):
		curr = max(curr, a[i])
		if curr < mem[i + 1]:
			count += 1
	return count

def max_chunks(arr):
	stack = []
	for a in arr:
		curr = stack[-1] if stack else -1
		while stack and stack[-1] > a:
			stack.pop()
		stack.append(max(curr, a))
	return len(stack)
	12304
	30124
	34







