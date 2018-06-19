#时间复杂度O(n)
#kumata 's code
'''
三个步骤：
1.找出最大最小值  
2.根据最大最小值差制造抽屉，把元素放进“抽屉”
3.把“抽屉”里面的元素拿出来重新排列
'''
import time
def count_sort(nums):
    start = time.time()    
    mmax, mmin = nums[0], nums[0]
    
    #第一个for循环找到最大值和最小值
    for i in range(1, len(nums)):
        if (nums[i] > mmax): 
            mmax = nums[i]
        elif (nums[i] < mmin): 
            mmin = nums[i]
    print('最大值:',mmax)
    print('最小值:',mmin)
    
    #“发抽屉”，制造多少个抽屉
    drawer = mmax - mmin + 1
    
    #刚开始抽屉里全部都是0
    counts = [0] * drawer
    print('抽屉数：',counts)   
    
    #通过index把元素往抽屉里面放
    for i in range (len(nums)):
        counts[nums[i] - mmin] = counts[nums[i] - mmin] + 1

    #把抽屉里面的元素拿出来重新排列
    #第一个for循环为抽屉的大小，第二个为抽屉里每个元素的个数，所以时间复杂度实为O(n)
    pos = 0
    for i in range(drawer):      
        for j in range(counts[i]):
            nums[pos] = i + mmin
            pos += 1
            
    t = time.time() - start
    return nums, t
