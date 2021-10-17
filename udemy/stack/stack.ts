class Stack {
  stack: number[];

  constructor() {
    this.stack = [];
  }

  push(val: number) {
    this.stack.push(val);
  }

  pop() {
    if (this.stack) {
      return this.stack.pop();
    }
  }
}

const stack = new Stack();
stack.push(1);
stack.push(2);
stack.pop();
stack.push(4);
stack.push(3);
console.log(stack.stack);
