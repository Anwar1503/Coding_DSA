# https://leetcode.com/problems/reverse-linked-list/description/


#TODO's
# Reverse a Linked List
# Detect a Cycle in a Linked List
# Find the Middle Node
# Middle of Linked List
# Linked List Cycle
# Find Start of Cycle
# Palindrome Linked List
# Reorder List


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append_ll(self,data):
        new_node = Node(data)

        if(self.head is None):
            self.head = new_node
            return 
        current = self.head
        
        while (current.next):
            current = current.next
        current.next = new_node

    def append_first(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append_at_pos(self,data,pos):
        new_node = Node(data)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return 
        current = self.head

        for i in range(pos -1):  
            current = current.next  

        new_node.next = current.next
        current.next = new_node


    def delete_ll(self,data):
        if self.head is None:
            return 
        current = self.head
        if( current == data):
            self.head = current.next
            return

        while(current.next):
            if(current.next.data == data):
                current.next = current.next.next
                return 
            current = current.next  

    def reverse_ll(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev


    def Display_ll(self):
        current = self.head

        while(current):
            print(current.data,end="->")
            current = current.next

        print("None")

if __name__ == "__main__":
    ll = LinkedList()
    ll.append_ll(10)
    ll.append_ll(20)
    ll.append_ll(30)
    ll.append_first(5)
    ll.append_at_pos(100,2)
    ##ll.delete_ll(20)
    ll.Display_ll()
    ll.reverse_ll()
    ll.Display_ll()         

