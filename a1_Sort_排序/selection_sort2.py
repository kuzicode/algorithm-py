
# 算法复杂度O(n^2)
# 方法：先写一个find数组最小元素的函数，再遍历把最小元素加进新数组
# 从小到大排

# 找出数组最小的值的index
def findsmallest(lis):
    smallest = lis[0]
    smallest_index = 0
    for i in range(len(lis)):
        if lis[i] < smallest:
            smallest = lis[i]
            smallest_index = i
    return smallest_index

def selection_sort(lis):
    new_lis = []
    for i in range(len(lis)):
        smallest_index = findsmallest(lis)
        new_lis.append(lis.pop(smallest_index))
    return new_lis

# 测试
if __name__ == '__main__':
    print(findsmallest([2,45,1,24,33]))
    print(selection_sort([2,45,1,24,33]))


