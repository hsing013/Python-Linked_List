#Harnoor Singh, October 2017
import random
class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None
        self.previous = None


class Linked:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    def get_size(self):
        return self.size
    def push_back(self, value):
        if self.head == None:
            self.head = Node(value)
        elif self.tail == None:
            self.tail = Node(value)
            self.tail.previous = self.head
            self.head.next = self.tail
        else:
            temp = self.tail
            self.tail = Node(value)
            temp.next = self.tail
            self.tail.previous = temp
        self.size += 1
    def push_front(self, value):
        if self.head is None:
            self.head = Node(value)
        elif self.tail is None:
            self.tail = self.head
            self.head = Node(value)
            self.tail.previous = self.head
            self.head.next = self.tail
            self.tail.next = None
        else:
            temp = self.head
            self.head = Node(value)
            self.head.next = temp
            temp.previous = self.head
        self.size += 1
    def pop_back(self):
        if self.head is None:
            return
        elif self.tail is None:
            head = None
        else:
            if self.tail.previous is not self.head:
                self.tail = self.tail.previous
                self.tail.next = None
            else:
                self.head.next = None
                self.tail = None
        self.size -= 1
    def pop_front(self):
        if self.head is None:
            return
        elif self.tail is None:
            self.head = None
        else:
            if self.head.next is self.tail:
                self.head = self.tail
                self.head.previous = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.previous = None
        self.size -= 1 
    def print(self):
        temp = self.head
        while temp != None:
            print(temp.value, end='')
            temp = temp.next
            if temp is not None:
                print(end=", ")
            else:
                print("\n", "Size: ", self.size, sep='')
    def at(self, index, flag):
        if self.size == 0:
            print("List is empty.")
            return
        if index >= self.size:
            print("Index is too large. Please input an index between 0-", self.size-1, ".", sep="")
            return None
        else:
            counter = 0
            current_node = self.head
            while (counter != index):
                current_node = current_node.next
                counter += 1
            if flag == 0:
                return current_node.value
            elif flag == 1:
                return current_node
            return None
    def modify_value_at(self, index, new_value):
        node = self.at(index, 1)
        if node is None:
            print("Can't modify value.")
            return
        else:
            node.value = new_value
    def insert_at(self, index, value): #will insert before this index
        node = self.at(index, 1)
        if node is None:
            return
        elif node is self.head:
            self.push_front(value)
        else:
            new_node = Node(value)
            new_node.next = node
            new_node.previous = node.previous
            node.previous.next = new_node
            node.previous = new_node
            self.size += 1
    def menu():
        print("\t1. Push back a value.")
        print("\t2. Push front a value.")
        print("\t3. Pop back a value.")
        print("\t4. Pop front a value.")
        print("\t5. Print value at x index.")
        print("\t6. Modify value at x index.")
        print("\t7. Insert value at x index.")
        print("\t8. Print the list")
        return -1

if __name__ == '__main__':
    #a = int(input())
    #b = int(input())
    l = Linked()
    l.push_back(9)
    #l.push_back(8)
    # l.push_back(87)
    # l.push_front(98)
    # l.push_front(65)
    # l.push_front(123)
    l.print()
    #l.pop_back()
    l.print()
    l.modify_value_at(0, -66)
    l.insert_at(0, -56)
    l.print()
    