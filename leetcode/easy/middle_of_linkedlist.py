# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        # fastがslowの二倍で進むのでfastが終了するときにはslowは中間にいる
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
