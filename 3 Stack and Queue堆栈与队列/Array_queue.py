
# 动态数组实现队列并不用内置方法

class ArrayQueue:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    # O(1)
    def first(self):
        if self.is_empty( ):
            raise ValueError( 'Queue is empty' )
        return self._data[self._front]
    
    # O(1)
    def dequeue(self):
        if self.is_empty( ):
            raise ValueError( 'Queue is empty' )
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        return answer
    
    # O(1)
    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # 如果满了开拓两倍空间
        pos = (self._front + self._size) % len(self._data)
        self._data[pos] = e
        self._size += 1
        
    def resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
        
    def printqueue(self):
        for i in range(self._size):
            pos = (self._front + self._size - 1 - i) % len(self._data)
            #print(str(i), ": ", str(pos))
            print(self._data[pos], end = " ")  
        print()

