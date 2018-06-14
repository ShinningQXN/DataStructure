import collections
import bisect
leetcode792
def numMatchingSubseq(S, words):
    """
    :type S: str
    :type words: List[str]
    :rtype: int
    """

    def match(word):
        pre = 0
        for c in word:
            index = bisect.bisect_left(map[c], pre)
            if index == len (map[c]):
                return False
            pre = map[c][index] + 1
        return True

    map = collections.defaultdict(list)
    for i in range (len (S)):
        map[S[i]].append (i)
    count = 0
    for word in words:
        if match (word):
            count += 1
    return count

print numMatchingSubseq('abcd', ['ac','d', 'aa', 'db'])