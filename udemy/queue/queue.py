from typing import Any
# ライブラリも存在する(appendとpopleft)、popを使えばstackのような使い方もできる
# from collections import deque


class Queue(object):
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, data) -> None:
        self.queue.append(data)

    def dequeue(self) -> Any:
        if self.queue:
            return self.queue.pop(0)


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    print(queue.queue)
