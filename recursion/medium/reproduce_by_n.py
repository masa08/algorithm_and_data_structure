class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def reproduceByN(head, n):
    iterator = head
    count = 0
    while iterator.next is not None:
        iterator = iterator.next
        count += 1

    for i in range(0, (count+1)*(n-1)):
        if (i == 0):
            current = head
            data0 = SinglyLinkedListNode(current.data)
            iterator.next = data0
        else:
            current = current.next
            data1 = SinglyLinkedListNode(current.data)
            iterator = iterator.next
            iterator.next = data1

    return head
