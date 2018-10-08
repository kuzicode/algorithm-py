'''
二分法查找在列表中的用户输入值，返回index
三种情况跳出循环体： LR相邻、LR位置重合、RL
算法时间复杂度为O(logn)
'''

def bi_search(lis,num):

    if len(lis) == 0:           # 判断边界条件
        return -1

    left, right = 0, len(lis)-1          # 列表的起始点和终点index

    while left <= right:
        # 取二分中心点，如果(left+right)为偶数, python自动将mid向下取整
        # 或 mid = (left + (right - left)) // 2
        mid = (left + right) // 2
        guess = lis[mid]

        if guess == num:
            return mid
        if guess < num:          # 猜小了，左点右移
            left = mid + 1
        else: # guess > num      # 猜大了，右点左移
            right = mid -1

    return None                  # 没有指定元素

# 测试
if __name__ == '__main__':

    num = int(input('please input a num:'))
    my_list = [1,2,3,4,5,6,7,8]
    bi_search(my_list,num)
