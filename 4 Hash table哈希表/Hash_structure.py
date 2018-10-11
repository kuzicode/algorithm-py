class HashMap(object):
    def __init__(self):
        # 初始化总表为，容量为2的表格（含两个子表）
        self.maps = BetterMap(2)
        self.num = 0        # 表中数据个数
      
    def get(self,k):        
        return self.maps.get(k)
      
    def add(self, k, v):
        # 若当前元素数量达到临界值（子表总数）时，进行重排操作
        # 对总表进行扩张，增加子表的个数为当前元素个数的两倍！
        if self.num == len(self.maps.maps): 
            self.resize()
         
        # 往重排过后的 self.map 添加新的元素
        self.maps.add(k, v)
        self.num += 1
         
    def resize(self):
        # 重排操作，添加新表, 注意重排需要线性的时间
        # 先建立一个新的表,子表数 = 2 * 元素个数
        new_maps = BetterMap(self.num * 2)
         
        for m in self.maps.maps:  # 检索每个旧的子表
            for k,v in m.items:   # 将子表的元素复制到新子表
                new_maps.add(k, v)
         
        self.maps = new_maps      # 令当前的表为新表