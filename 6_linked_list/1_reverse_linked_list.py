# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val}, {self.next})"
        

class Solution:
    def reverseList(self, head):
        # how do you set up a linked list so that you can access the individual nodes
        # do you create an instance of the ListNode class and then call methods? no.
        # do you create an instance of the ListNode class and then call attributes w/in the function? maybe.
        # do you pass in an instance (head) and then call attributes on that instance? perhaps.
        pass
        





head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

head = [1, 2, 3, 4, 5]
print(Solution().reverseList(head))

head = [1, 2]
print(Solution().reverseList(head))