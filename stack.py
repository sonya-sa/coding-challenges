class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.insert(0, item)
    
    def pop(self):
        return self.items.pop(0)
    
    def peek(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)

def par_checker(symbol_string):
        s = Stack()
        balanced = True
        index = 0
        while index < len(symbol_string) and balanced:
            symbol = symbol_string[index]
            if symbol == "(":
                s.push(symbol)
            else:
                if s.is_empty():
                    balanced = False
                else:
                    s.pop()

            index = index + 1

        if balanced and s.is_empty():
            return True
        else:
            return False

print(par_checker('((()))'))
print(par_checker('(()'))

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Deque:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def add_front(self, item):
        self.items.append(item)
    
    def add_rear(self, item):
        self.items.insert(0,item)
    
    def remove_front(self):
        return self.items.pop()
    
    def remove_rear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)

def pal_checker(a_string):
    char_deque = Deque()
    for ch in a_string:
        char_deque.add_rear(ch)
    
    still_equal = True
    while char_deque.size() > 1 and still_equal:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
    if first != last:
        still_equal = False
    
    return still_equal
print(pal_checker("lsdkjfskf"))
print(pal_checker("radar"))

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, new_data):
        self.data = newdata
    
    def set_next(self, new_next):
        self.next = new_next