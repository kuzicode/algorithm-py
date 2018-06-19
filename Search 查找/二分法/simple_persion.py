'''
简单方法
二分法查找在列表中的用户输入值，返回index
三种情况跳出循环体： LR相邻    LR位置重合   RL
算法时间复杂度为O(logn)

'''

def bi_search(lis,num):
    
    if len(lis) == 0:           #判断边界条件
        return -1
　　
    left, right = 0, len(lis)-1          #列表的起始点和终点
  
    while left <= right:

        mid = (left + (right - left)) // 2     #取二分中心点，或 mid = (left + right) // 2

        if num < lis[mid]:               #右点左移
            right = mid - 1 
        elif num > lis[mid]:             #左点右移
            left = mid + 1 
        else:                            #num == lis[mid]    
            return mid

    return -1

num = int(input('please input a num:'))
alist = [1,2,3,4,5,6,7,8]
bi_search(alist,num)