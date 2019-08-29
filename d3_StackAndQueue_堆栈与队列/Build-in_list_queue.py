
# 使用Python的内建类型list列表实现很方便

class Queue():
    def __init__(self):
        self.items = []

    # 加于队列后
    def enqueue(self,item):
        return self.items.append(item)

    # 队列头pop出来
    def dequeue(self,item):
        return self.items.pop(0)

    # 判断是否空队列
    def is_empty(self):
        return self.size() == 0

    # 返回队列长度
    def size(self):
        return len(self.items)

    # 打印队列
    def printqueue(self):
        for i in self.items:
            print(i,end=' ')



# 测试
if __name__ == "__main__":
    q = Queue()
    print(q)
    q.enqueue('aa')
    q.enqueue('bb')
    print(q.size())
    print(q.is_empty())
    q.printqueue()



