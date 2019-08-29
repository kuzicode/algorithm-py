# O(nlogn)
# pivot枢纽，low和high为起点终点

'''
步骤：
一、选择基准值pivot(枢纽)
二、数组分为两个子数组：小于基准值的元素和大于基准值的元素
三、对子数组分而治之，快速排序
'''

def quick_sort(lis):
    
    # 解决问题的返回条件：数组剩下2个单位
    if len(lis) < 2:
        return lis
    
    # 分解过程
    else:
        pivot = lis[0]                                      # 挑选第一个元素为基准值
        left = [i for i in lis[1:] if i <= pivot]           # 小于pivot的元素
        right = [i for i in lis[1:] if i > pivot]           # 大于pivot的元素
        
    # 递归分治后合并
    return quick_sort(left) + [pivot] + quick_sort(right)   # 注意pivot写成列表的形式才能连接

# 测试
if __name__ == '__main__':
    print(quick_sort([4,2,5,6,1]))

