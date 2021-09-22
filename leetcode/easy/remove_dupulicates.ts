import { ListNode } from "../common/common";

function deleteDuplicates(head: ListNode | null): ListNode | null {
  if (head === null) return null;

  let curr = head;

  while (head && head.next) {
    if (head.val == head.next.val) {
      head.next = head.next.next;
    } else {
      head = head.next;
    }
  }

  return curr;
}
