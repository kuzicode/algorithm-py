'''
Fibonacci（斐波那契数列）
1,1,2,3,5,8,13,25....
'''
#使用递归
#算法复杂度：O(2^n) 注：该递归算法复杂度较高，且运行速度较慢    
#定义实现函数
def fib(n):
    if n <= 1:
        return n
    else: 　
        return(fib(n-1) + fib(n-2))

# 获取用户输入 
num = int(input("您要输出几项? "))

# 检查输入的数字是否正确
if num <= 0:
    print("输入正数")
else:
    print("斐波那契数列:")
    for i in range(num):
        print(fib(i))


'''

#使用简单的函数
#算法复杂度更低的fibonacci数列
#算法复杂为O（n）
def fib(n):
    num, a, b = 0, 0, 1
    while num < n:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

'''