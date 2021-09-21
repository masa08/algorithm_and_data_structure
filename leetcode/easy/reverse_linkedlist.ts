import { ListNode } from "../common/common";

function reverseList(head: ListNode | null): ListNode | null {
  let reversed = null;
  let current = head;

  while (current) {
    let nextTemp = current.next;
    current.next = reversed;
    reversed = current;
    current = nextTemp;
  }

  return reversed;
}
