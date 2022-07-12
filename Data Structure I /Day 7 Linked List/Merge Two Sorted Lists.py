from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time:   O(max(n, m))
    Memory: O(1)
    """

    def mergeTwoLists(self, first: Optional[ListNode], second: Optional[ListNode]) -> Optional[ListNode]:
        if first is None or second is None:
            return first or second

        dummy = curr = ListNode()
        while first and second:
            if first.val < second.val:
                curr.next = first
                first = first.next
            else:
                curr.next = second
                second = second.next
            curr = curr.next

        curr.next = first or second
        return dummy.next
