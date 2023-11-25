# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        
        return list1.val, list1.next, list2.val, list2.next


a = ListNode(1)
b = ListNode(2)
print(Solution().mergeTwoLists(a, b))