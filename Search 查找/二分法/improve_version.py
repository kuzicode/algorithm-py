'''
改进方案：如果我要找一个数组中相同数字最前面的那个数字。
比如lis = [1,2,2,2,2,3,3,5,6],用上面的代码会返回index为4，
下面代码解决如何返回相同元素的最前一个

改进版本经典方法，这种方法更加好写
把常规方法的right = mid -1 和left = mid +1修改
找不到返回None
'''

def bi_search2(lis, num):
   
    # 这个程序中这一条判断边界非常重要
    if len(lis) == 0:
        return -1
    
    # 判断二分条件
    left, right = 0, len(lis) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if lis[mid] == num:
            right = mid
        elif lis[mid] < num:
            left = mid
        elif lis[mid] > num:
            right = mid
    
    # 在这里返回
    if lis[left] == num:
        return left
    if lis[right] == num:
        return right
    
    return None

if __name__ == '__main__':
    num = int(input('please input a num:'))
    my_list = [1,2,2,2,2,6,7,8]
    bi_search2(my_list,num)