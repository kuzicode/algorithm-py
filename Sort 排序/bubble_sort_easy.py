#算法时间复杂度为O（n^2）
'''
为体现冒牌排序细节的不同，
我写出简单的冒泡排序方法:bubble_sort_easy
和改进后的冒泡排序方法:bubble_sort_imp
'''
#kumata's code
#简单的冒泡排序方法
#它的问题是当列表本来的顺序就是比较完好；仍会花费复杂的时间空间来排序

def bubble_sort_easy(nums: list):
    for i in range(len(nums)):
        # 嵌套的二层循环的index从0开始，所以后面要len(nums)-i-1
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]   #交换
    return nums



