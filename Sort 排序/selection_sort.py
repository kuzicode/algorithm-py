#kumata's code
#算法复杂度O(n^2)
#找到最小的元素就和第一个index交换
#从小到大排

import time

def selection_sort(nums=list):
    start = time.time()
    
    #第一层选择第n小的元素下标
    for i in range(len(nums)):    # n 
        pos_min = i     # Index
        #第二层遍历找出需要交换的元素下标
        for j in range(i + 1,len(nums)):
            if nums[pos_min] > nums[j]:
                pos_min = j
        #交换嘻嘻
        nums[i],nums[pos_min] = nums[pos_min],nums[i]
        
    t = time.time() - start
    return nums,t