# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        # Traverse the list
        while current and current.next:
            # If the current value equals the next value, skip the duplicate
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                # Move to the next node if no duplicate
                current = current.next
        return head

