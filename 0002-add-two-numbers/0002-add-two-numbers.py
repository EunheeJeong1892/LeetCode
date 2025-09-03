# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        print(l1)
        reversed_1 = self.getReversedNumbers(1, l1)
        reversed_2 = self.getReversedNumbers(1, l2)

        total = str(reversed_1 + reversed_2) 
        head = None
        for digit in total: 
            node = ListNode(int(digit))
            node.next = head
            head = node
        
        return head
    
    def getReversedNumbers(self,digit:int, l:Optional[ListNode]):
        result = 0
        if l.next:
            result = self.getReversedNumbers(digit*10,l.next)
        result += digit * l.val
        return result
        
        

