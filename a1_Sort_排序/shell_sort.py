#相比插入排序，shell排序更适合用于处理data更大的数组

import time

def shell_sort(nums):
    start = time.time()

    gap = len(nums)       #先指定len长度给gap后续对gap进行分组子序列
    length = len(nums)

    #while用于处理每个大轮的sort
    while (gap > 0):
        
        #两个for循环与插入排序同理
        for i in range(gap, length):
            for j in range(i, gap - 1, -gap):
                if (nums[j - gap] > nums[j]):
                    nums[j], nums[j - gap] = nums[j - gap], nums[j]

        if (gap == 2): 
            gap = 1
        else:
            gap = gap // 2    #每一次比上一次大概扩大两倍的分组子序列

    t = time.time() - start
    return nums, t           