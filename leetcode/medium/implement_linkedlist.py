class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def _getLength(self) -> int:
        curr_node = self.head
        length = 0

        while curr_node:
            length += 1
            curr_node = curr_node.next

        return length

    def _print(self) -> int:
        curr_node = self.head

        while curr_node:
            print(curr_node.val)
            curr_node = curr_node.next

    def get(self, index: int) -> int:
        curr_node = self.head
        curr_idx = 0
        while curr_node:
            if curr_idx == index:
                return curr_node.val
            curr_node = curr_node.next
            curr_idx += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        curr_node = self.head

        if curr_node is None:
            self.head = new_node
            return

        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)

        if index == 0:
            self.addAtHead(val)
            return

        if index == self._getLength():
            self.addAtTail(val)
            return

        curr_node = self.head
        curr_idx = 0
        prev = None

        while curr_idx != index and curr_node.next is not None:
            prev = curr_node
            curr_node = curr_node.next
            curr_idx += 1

        temp = prev.next
        prev.next = new_node
        new_node.next = temp

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
        else:
            curr_node = self.head
            curr_idx = 0
            prev = None

            while curr_idx != index and curr_node.next is not None:
                prev = curr_node
                curr_node = curr_node.next
                curr_idx += 1

            if curr_idx == index:
                prev.next = curr_node.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
