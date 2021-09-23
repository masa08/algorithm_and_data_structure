import { TreeNode } from "../common/common";

function inorderTraversal(root: TreeNode | null): number[] {
  function _inorderTraversal(root: TreeNode | null, arr: number[]): void {
    if (root != null) {
      _inorderTraversal(root.left, arr);
      arr.push(root.val);
      _inorderTraversal(root.right, arr);
    }
  }

  let arr = [];
  _inorderTraversal(root, arr);

  return arr;
}
