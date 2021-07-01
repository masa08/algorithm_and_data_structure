class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def getLength(head):
    iterator = head
    length = 0
    while iterator is not None:
        length += 1
        iterator = iterator.next
    return length


def getNodeAt(head, index):
    iterator = head
    for i in range(index):
        iterator = iterator.next
    return iterator


def findMergeNode(headA, headB):
    lenA = getLength(headA)
    lenB = getLength(headB)
    if lenA >= lenB:
        headA = getNodeAt(headA, lenA-lenB)
    else:
        headB = getNodeAt(headB, lenB-lenA)

    answer = -1
    iteratorA = headA
    iteratorB = headB
    while iteratorA is not None:
        if (iteratorA.data != iteratorB.data):
            answer = -1
        else:
            if answer == -1:
                answer = iteratorA.data
        iteratorA = iteratorA.next
        iteratorB = iteratorB.next

    return answer
