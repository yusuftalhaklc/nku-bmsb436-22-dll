"""
https://nku-bmsb436-22-dll.yusuftalhaklc.com
1210606019 - Yusuf Talha Kılıç
BMSB436. Python Programlamaya Giriş - 22:nolu ödev
'22. Çift yönlü bir bağlı listeyi (doubly linked list) kopyalayan ve tersine çeviren bir fonksiyon
yazın.'
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def __repr__(self):
        return str(self.data)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def from_list(self, data_list):
        self.head = None
        self.tail = None
        self.size = 0
        for item in data_list:
            self.append(item)
        return self
    
    def copy(self):
        copied_list = DoublyLinkedList()
        current = self.head
        while current:
            copied_list.append(current.data)
            current = current.next
        return copied_list
    
    def reverse(self):
        if not self.head or self.size <= 1:
            return self
        
        current = self.head
        self.head, self.tail = self.tail, self.head
        
        while current:
            temp = current.next
            current.next, current.prev = current.prev, current.next
            current = temp
        
        return self
    
    def copy_and_reverse(self):
        copied_list = self.copy()
        copied_list.reverse()
        return copied_list