#kumata's code
#算法时间复杂度O(n^2)
#从小到大排

import time

def insert_sort(nums):
    start = time.time()
    
    #一张张摸牌,拿到手中
    for sort_inx in range(1,len(nums)):   #从1开始
        unsort_inx = sort_inx
        #当需要排序的index大于0且未排index前一个大于后一个时：
        while unsort_inx > 0 and nums[unsort_inx - 1] > nums[unsort_inx]:
            #前后交换
            nums[unsort_inx - 1], nums[unsort_inx] =  nums[unsort_inx], nums[unsort_inx - 1]  
            unsort_inx = unsort_inx - 1  #unsort下标更新
            
    t = time.time() - start
    return nums,t