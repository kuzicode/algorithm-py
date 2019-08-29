#思路：遍历找出分别找出最小和最大值，然后使用remove()去掉，最后求数组总和再除以len(values)
values =  [8,9,5,10,5,8,7,9,9.5]
'''
这种方法用逻辑的思路实现，麻烦了点但是可以训练下思维
#求最小分
small_pos = values[0]
for small_grade in values:
    if small_grade < small_pos:
        small_pos = small_grade
print('最小分：%d' % small_pos)
​
#求最大分
high_pos = values[0]
for high_grade in values:
    if high_grade > high_pos:
        high_pos = high_grade
print('最大分：%d' % high_pos)
​
values.remove(values[small_pos])
values.remove(values[high_pos])
print(values)
'''

#不好意思，python内置可以直接搞定
values.remove(max(values))
values.remove(min(values))
a = sum(values)/len(values)
print(a)

