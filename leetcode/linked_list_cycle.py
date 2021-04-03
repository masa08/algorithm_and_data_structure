# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 循環しているのであれば、fastはいずれslowと一致するはず
# https://zenn.dev/hcrane/articles/2a04fd3e479745601106
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head.next if head else None
        fast = slow.next if slow else None

        while True:
            if slow and fast:
                if slow == fast:
                    return True
                else:
                    slow = slow.next
                    fast = fast.next.next if fast.next else None
            else:
                return False

# 逐一setにheadを押し込んで、head.nextが既存のsetと一致するのであれば、循環していると判断する。
# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         s = set()
#         while(head):
#             if head in s:
#                 return True
#             s.add(head)
#             head = head.next
#
#         return False

