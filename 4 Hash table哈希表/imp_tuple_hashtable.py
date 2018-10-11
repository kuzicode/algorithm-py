'''
将总查询表分割为若干段较小的列表，比如100个子段。
通过hash函数求出某个键的哈希值，再通过计算，得到往哪个子段中添加或查找。
相对于从头开始搜索列表，时间会极大的缩短。

改进版本：
尽管get操作的增长依然是线性，但BetterMap类使得我们离哈希表更近一步：
'''


class BetterMap(object):
      # 利用 LinearMap 对象作为子表，建立更快的查询表
    def __init__(self,n=100):
        self.maps = []          # 总表格
        for i in range(n):      # 根据n的大小建立n个空的子表
            self.maps.append(LinearMap())
      
    def find_map(self,k):       # 通过hash函数计算索引值
        index = hash(k) % len(self.maps)
        return self.maps[index] # 返回索引子表的引用     
 
     # 寻找合适的子表（linearMap对象）,进行添加和查找
    def add(self, k, v):
        m = self.find_map(k)        
        m.add(k,v)
     
    def get(self, k):
        m = self.find_map(k)
        return m.get(k)