"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

from singly_linked_list import LinkedList

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         try:
#             self.storage.append(value)
#         finally:
#             self.size = self.size + 1

#     def pop(self):
#         try:
#             value = self.storage.pop()
#         except IndexError:
#             value = None
#         else:
#             self.size = self.size - 1

#         return value

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        try:
            self.storage.add_to_tail(value)
        finally:
            self.size = self.size + 1

    def pop(self):
        try:
            value = self.storage.remove_tail()
        except IndexError:
            value = None
        else:
            if self.size > 0:
                self.size = self.size - 1

        return value