class Queue {
  queue: number[];

  constructor() {
    this.queue = [];
  }

  enqueue(val: number) {
    this.queue.push(val);
  }

  dequeue() {
    if (this.queue) {
      this.queue.shift();
    }
  }
}

const quque = new Queue();
quque.enqueue(1);
quque.enqueue(2);
quque.enqueue(4);
quque.enqueue(5);
quque.dequeue();

console.log(quque.queue);
