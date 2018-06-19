#改进的冒泡排序
'''
1.加入time计时runing时间
2.加入flag判断列表是否已经不需要继续排序，提高效率
'''
def bubble_sort_imp(nums=list):
    import time
    start = time.time()  #开始时间  
    for i in range(len(nums)): # 当 n pass
        
        is_sorted = True  # 立个flag，当已经排好序的情况时引入Ture的is_sort
        
        for j in range(0, len(nums) - i - 1):
            if (nums[j + 1] < nums[j]):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]  #交换
                
                is_sorted = False    #立个False的flag
        
        if (is_sorted): break    #当不需用到嵌套二层for时退出，提高效率
            
    t = time.time() - start  #记下运行时间
    return nums,t

