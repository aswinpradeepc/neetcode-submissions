# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}
        curr = head
        i=0
        while curr:
            if not seen.get((curr.val, curr.next)):
                seen[(curr.val, curr.next)] = i
            else:
                # return seen[(curr.val, curr.next)]
                return True
            curr = curr.next
            i+=1
        return False

                   