#列表和二维数组读取一行或一列的方法

sample_list = [[67, 22,  3, 81, 25],
               [13, 78, 94, 70, 68],
               [98, 27,  3, 69, 37],
               [50, 69, 40, 86, 33]]

#获取3、4行
hang_3 = sample_list[2]
hang_4 = sample_list[3]

#获取3、4列
#我们需要用列表解析的方法读取列：
lie_3 = [x[2] for x in sample_list]
lie_4 = [x[3] for x in sample_list]

print(hang_3)
print(hang_4)

print(lie_3)
print(lie_4)

#而对于数组，可以直接读取：
import numpy as np
lie_3 = np.array(sample_list)
print(lie_3[:,2])

'''
输出结果
[98, 27, 3, 69, 37]
[50, 69, 40, 86, 33]

[3, 94, 3, 40]
[81, 70, 69, 86]

[ 3 94  3 40]
'''