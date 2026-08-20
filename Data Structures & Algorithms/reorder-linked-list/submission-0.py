# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head:
            return []

        store = []
        curr = head
        while curr:
            store.append(curr)
            curr = curr.next
        

        i = 0  
        n = len(store) 
        j = n -1
        while i<j:
            store[i].next=store[j]
            i+=1
            if i==j:
                break
            store[j].next=store[i]
            j-=1
        store[i].next = None