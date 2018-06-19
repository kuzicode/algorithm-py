'''
O(nlogn)
pivot枢纽，low和high为起点终点
'''
#划分分区（非就地划分）
def partition(nums=list):
    pivot = nums[0]                             #挑选枢纽
    lo = [x for x in nums[1:] if x < pivot]     #所有小于pivot的元素
    hi = [x for x in nums[1:] if x >= pivot]    #所有大于pivot的元素
    return lo,pivot,hi

#快速排序
def quick_sort(nums=list):
    #被分解的Nums小于1则解决了
    if len(nums) <= 1:
        return nums

    #分解    
    lo,pivot,hi = partition(nums)

    # 递归（树），分治，合并
    return quick_sort(lo) + [pivot] + quick_sort(hi)