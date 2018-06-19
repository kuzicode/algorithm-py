#递归
#算法复杂度：O（2^n）
'''
设定三根棒子从左到右为：x、y、z
思路：
第一步：x上的（n-1）个盘子借助 z 到 y上
第二步：y上的（n-1）个盘子借助 x 到 z上
'''
def hanio(n,x,y,z):
    if n == 1:
        print(x,'-->',z)       #如果只有一层，直接从x移动到z
    else:
        hanio(n-1,x,z,y)    #将n-1个盘子从x移动到y
        print(x,'-->',z)       #最底下的盘子从x移动到z 
        hanio(n-1,y,x,z)    #将n-1个盘子从y移动到z

n = int(input('please input the floor:'))
hanio(n,'x','y','z')