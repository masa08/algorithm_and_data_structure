# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head

        curr = head

        while head and head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next

        return curr.next if curr.val == val else curr
