# 函数上会标明该方法的时间复杂度
# 动态数组的类
import ctypes

class DynamicArray:
    
    def __init__ (self):
        # Create an empty array
        self._n = 0   # size
        self._capacity = 10    # 先给个10
        self._A = self._make_array(self._capacity)
        
    def __len__ (self):
        return self._n
    
    def is_empty(self):
        return self._n == 0
    
    # O(1)
    def __getitem__ (self, k):
        if not 0 <= k < self._n:
            raise ValueError('invalid index') 
        return self._A[k]
       
    # O(1) 
    def append(self, obj):
        if self._n == self._capacity:    # 首先要判断该容器是否放得下
            self._resize(2 * self._capacity)
        self._A[self._n] = obj    
        self._n += 1
        
    def _make_array(self, c):
        return (c * ctypes.py_object)( )
    
    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c   

    # O(n)
    def insert(self, k, value):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):    # 从后往前一个一个往后移
            self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1
     
    # O(n)    
    def remove(self, value):
        for k in range(self._n):
            if self._A[k] == value:     # 一个个查value
                for j in range(k, self._n - 1):
                    self._A[j] = self._A[j+1]   # 再一个个移上来
                self._A[self._n - 1] = None
                self._n -= 1
                return
        raise ValueError( 'value not found' )
    
    def _print(self):
        for i in range(self._n):
            print(self._A[i], end = ' ')
        print()

# 测试
if __name__ == '__main__':
    mylist = DynamicArray()
    print ('size was: ', str(len(mylist)))
    mylist.append(10)
    mylist.append(20)
    mylist.append(30)
    mylist.insert(0, 0)
    mylist.insert(1, 5)
    mylist.insert(3, 15)
    mylist._print()
    mylist.remove(20)
    mylist._print()
    print ('size is: ', str(len(mylist)))