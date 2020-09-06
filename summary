LRU缓存机制解题思路：

题目：
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

一、题目理解
1、获取数据，代表最近使用过该部分数据，因此，当获取到的数据的同时，应该将数据向前移动，或者是提升数据的权限，避免被当作不使用数据删除掉；
2、写入数据，其实也包含获取数据的一些操作，如果数据已经存在，则应该将该数据向前移动（类似于获取数据时的操作），如果数据不存在，则在最前面位置重新插入数据即可，插入后判断容量，如果超出上限则删除尾部数据（不常用数据）
二、编写思路
1、为了实现O(1)时间复杂度查找和插入数据，因此可以选择哈希表来存放（key,value）对，可以保证O(1)时间复杂度内定位数据。
2、在查找和写入数据时，涉及到数据的移动、删除等操作，选择双向链表结构可以保证在O(1)时间复杂度要求内，对数据进行操作，直接达到结果，不需要过多的挪动其他数据元素；
3、初始化链表时，可以先构造head和tail两个节点，便于元素的操作。
三、示例代码（可执行）
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.hash_map:
            node = self.hash_map[key]
            # 先删除节点
            node.prev.next = node.next
            node.next.prev = node.prev
            # 移动节点到头部
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            # 更新key对应的value值
            node.value = value
            # 先删除节点
            node.prev.next = node.next
            node.next.prev = node.prev
            # 移动节点到头部
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
        else:
            node = DLinkedNode(key, value)
            self.hash_map[key] = node
            # 插入最新数据到头部
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            self.size += 1
            if self.size > self.capacity:
                # 删除尾部元素
                self.hash_map.pop(self.tail.prev.key)
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev


if __name__ == '__main__':
    obj = LRUCache(2)
    obj.put(2, 1)
    obj.put(2, 2)
    param_1 = obj.get(1)
    obj.put(3, 3)
    param_1 = obj.get(2)
    print('end')
