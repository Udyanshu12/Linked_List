from node import Node


class LinkedList(Node):
    
    def __init__(self, node):
        super().__init__(node)
        self.head = node
        self.tail = node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        return True

    def pop(self):
        if self.head == None:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, node):
        if self.head == None:
            self.tail = node
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1
        return True

    def pop_first(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, node):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(node)
        elif index == self.length:
            self.append(node)
        else:
            temp = self.get(index-1)
            node.next = temp.next
            temp.next = node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            self.pop_first()
        elif index == self.length-1:
            self.pop()
        else:
            prev = self.get(index - 1)
            temp = prev.next
            prev.next = temp.next
            temp.next = None
        self.length -= 1

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length+1):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
