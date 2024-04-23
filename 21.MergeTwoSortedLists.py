# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
    # Create a dummy node to simplify code
        dummy = ListNode()
        current = dummy

        # Traverse both lists
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # If one of the lists is not empty, append the remaining elements
        if l1 is not None:
            current.next = l1
        else:
            current.next = l2

        return dummy.next
