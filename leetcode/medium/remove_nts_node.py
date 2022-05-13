# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        # nの分fastをずらす
        for i in range(n): fast = fast.next
        # n = length-1の場合
        if not fast: return head.next

        # ずらした分slowを進めると、削除対象手前まで進む
        while fast.next:
            fast = fast.next
            slow = slow.next

        # リンクを付け替える
        slow.next = slow.next.next

        return head
