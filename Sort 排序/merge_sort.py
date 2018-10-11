'''
名字很多：归并排序/合并排序/二分排序
算法时间复杂度 O(logn)
递归
两个步骤：1.拆分 2.合并
'''

def merge_sort(nums=list):

    # 取mid以及左右两个数组
    mid = len(nums)//2
    left_nums,right_nums = nums[:mid],nums[mid:]

    # 递归分治
    if len(left_nums) > 1:
        left_nums = merge_sort(left_nums)
    if len(right_nums) > 1:
        right_nums = merge_sort(right_nums)

    # 合并
    res = []
    while left_nums and right_nums:            # 两个都不为空的时候
        if left_nums[-1] >= right_nums[-1]:    # 尾部较大者
            res.append(left_nums.pop())
        else:
            res.append(right_nums.pop())
    res.reverse() # 倒序
    return (left_nums or right_nums) + res     # 前面加上剩下的非空nums