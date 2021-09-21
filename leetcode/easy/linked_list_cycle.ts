class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function hasCycle(head: ListNode | null): boolean {
  let slow = head ? head.next : null;
  let fast = slow ? slow.next : null;

  while (true) {
    if (slow && fast) {
      if (slow == fast) {
        return true;
      } else {
        slow = slow.next;
        fast = fast.next ? fast.next.next : null;
      }
    } else {
      return false;
    }
  }
}
