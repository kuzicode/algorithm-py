""" 
线性表结构
建立一个线性表，使用元组来实现 key-value 的映射关系
"""
class LinearMap(object):

    def __init__(self):
         self.items = []
     
    # 往表中添加元素    
    def add(self, k, v):  
        self.items.append((k,v))

    # 线性方式查找元素
    def get(self, k): 
        for key, value in self.items:      
            if key == k:      # 键存在，返回值，否则抛出异常
                return value
        raise KeyError

'''
我们可以在使用add添加元素时让items列表保持有序，而在使用get时采取二分查找方式，时间复杂度为O(log n)。 
然而往列表中插入一个新元素实际上是一个线性操作，所以这种方法并非最好的方法。
同时，我们仍然没有达到常数查找时间的要求。
'''