# TODO: 理解して自分なりにかけるように
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)  # resultを返す用のdummyNodeを定義
        dummy.next = head
        pre = dummy
        cur = head

        while cur:
            if cur.next and cur.val == cur.next.val:
                # 重複の最後までcurを動かす
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                pre.next = cur.next  # 重複の最後の次の値(重複していない値)をpre.nextに
            else:
                pre = pre.next
            cur = cur.next

        return dummy.next
