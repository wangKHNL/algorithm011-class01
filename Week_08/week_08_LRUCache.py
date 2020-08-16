from typing import List
import operator
import numpy as np
import queue

"""
LRU缓存机制
"""


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


# Your LRUCache object will be instantiated and called as such:
if __name__ == '__main__':
    obj = LRUCache(2)
    obj.put(2, 1)
    obj.put(2, 2)
    param_1 = obj.get(1)
    obj.put(3, 3)
    param_1 = obj.get(2)
    print('end')
