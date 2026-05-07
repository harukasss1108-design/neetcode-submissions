# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # tail:Optional[ListNode]
        # while (tail.next !=null):
        #     tail=tail.next
        prev = None
        #curr: Optional[ListNode]= head

        while head:
            temp: Optional[ListNode] = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
