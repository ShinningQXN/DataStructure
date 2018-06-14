# 第四轮, 两个字符串, 一个字符串比另一个多一个字母, 其余出现顺序相同, 返回那个字母,
# follow
# up: 出现顺序不一定相同, 返回那个字母,
# follow
# up: 如果字符串特别大, 怎么办?

# 和这道题相同
# https://leetcode.com/problems/missing-number/description/
def missingLetter(arr1, arr2):
    xor = 0
    for i in range(len(arr1)):
        xor = xor ^ ord(arr1[i]) ^ ord(arr2[i])
    return chr(xor ^ 0 ^ ord(arr2[len(arr2) - 1]))

print missingLetter(['a','B'], ['a', 'B','c'])