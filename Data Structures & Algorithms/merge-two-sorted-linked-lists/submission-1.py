# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        acurr = list1
        bcurr = list2
        ccurr = ListNode()
        chead=ccurr

        while acurr and bcurr:
            temp=ListNode()
            if acurr.val < bcurr.val:
                temp.val = acurr.val
                ccurr.next = temp
                ccurr=temp
                acurr=acurr.next
            elif bcurr.val <= acurr.val:
                temp.val = bcurr.val
                ccurr.next = temp
                ccurr=temp
                bcurr=bcurr.next
        ccurr.next = acurr or bcurr
        return chead.next
            
        