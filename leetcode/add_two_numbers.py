# pythonの参照について
# https: // qiita.com/happyisland44/items/ac516aad49809caf74ea
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_num = []
        l2_num = []

        while l1:
            l1_num.append(str(l1.val))
            l1 = l1.next

        while l2:
            l2_num.append(str(l2.val))
            l2 = l2.next

        l1_int = int(''.join(l1_num[::-1]))
        l2_int = int(''.join(l2_num[::-1]))

        final_num = l1_int + l2_int
        final_num_str = str(final_num)[::-1]

        l3 = l4 = ListNode(int(final_num_str[0]))

        for digits in range(1, len(final_num_str)):
            l3.next = ListNode(int(final_num_str[digits]))
            l3 = l3.next

        return l4
