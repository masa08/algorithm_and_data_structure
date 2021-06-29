class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertNodeInSorted(head, data):
    iterator = head

    if data < iterator.data:
        newNode = SinglyLinkedListNode(data)
        newNode.next = head
        return newNode

    while iterator.next is not None:
        if data < iterator.next.data:
            temp = iterator.next
            iterator.next = SinglyLinkedListNode(data)
            iterator.next.next = temp
            return head
        iterator = iterator.next

    iterator.next = SinglyLinkedListNode(data)
    return head
