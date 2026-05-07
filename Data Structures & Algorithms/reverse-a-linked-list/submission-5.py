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
        curr: Optional[ListNode]= head

        while curr:
            temp: Optional[ListNode] = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
