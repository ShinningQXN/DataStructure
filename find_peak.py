有一个曲线，曲线的形状是先递减再增加，找曲线的最低点，如果只考虑int怎么做，如果考虑double怎么做

【细节】：
二分法，如果最后只剩两个，每次都会落在第二个值，就会出现死循环
比如，the last position中， 或者当start或者end出现负数时候

解法一
def find_peak(nums):
	start, end = 0, len(nums) - 1
	while start < end:
		mid = start + (end - start) / 2
		if nums[mid] < nums[mid + 1]:
			start = mid + 1
		else:
			end = mid
	return start

解法二
def fun(x):
	return x * (x - 3)
	return x * x

def find_peak(fun, start, end):
	while start + 1 < end:
		mid = start + (end - start) / 2
			if fun(mid) < fun(mid + 1):
				start = mid + 1
			else:
				end = mid
	return start if fun(start) : 
【这里之所以要start + 1 end】因为 如果有-1， 0， 则mid为0，而不是-1

double three_devide(double low,double up)  
{  
    double m1,m2;  
    while(up-low>=eps)  
    {  
        m1=low+(up-low)/3;  
        m2=up-(up-low)/3;  
        if(f(m1)<=f(m2))  
            up=m2;  
        else  
            low=m1;  
    }  
    return (m1+m2)/2;  
}  

[1,2,4,5,2,1]