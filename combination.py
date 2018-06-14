# 给一个integer array 表示不同符号的个数, 和输入n, 返回所有可能的n个符号的组合(不在乎顺序)
# [2,1,1]
# follow up: 返回这些组合的个数, 优化时间空间复杂度

def dfs(nums, n, path, result, index):
    if len (path) == n:
        result.append (path)
        return
    for i in range (index, len (nums)):
        for j in range (1, nums[i] + 1):
            dfs (nums, n, path + [i for _ in range (1, j + 1)], result, i + 1)


def combination(nums, n):
    result = []
    dfs (nums, n, [], result, 0)
    return result


print combination ([2, 1, 1], 3)
print combination([1,2], 2)
