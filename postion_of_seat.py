
# 1. 一些人坐在椅子上，新来的人要坐在离两侧人尽量远的位置，然后要求在线算法。这是一道面经题，用heap维护剩余区间就可以了。然后在线其实是个follow up。
# python 的heap该怎么做

# https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python
def position_of_seat(seats):
    position = -1
    pre = -1
    interval = 0
    for i in range (len (seats)):
        seat = seats[i]
        if seat == 1:
            if pre != -1 and i - pre - 1 > interval:
                position = (i + pre) / 2 #median is (a+b)/2, not (a-b)/2
                interval = i - pre - 1
                # print i, pre
            pre = i
    return position


print position_of_seat ([])
print position_of_seat ([1])
print position_of_seat ([1, 1])
print position_of_seat ([1, 0, 1, 0, 0, 1])
print position_of_seat ([1, 1, 0, 1, 0, 0, 0, 1])





			
			