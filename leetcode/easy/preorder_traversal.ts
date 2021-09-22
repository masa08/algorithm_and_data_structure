import { TreeNode } from "../common/common";

function preorderTraversal(root: TreeNode | null): number[] {
  function _preorderTraversal(root: TreeNode | null, arr: number[]): void {
    if (root != null) {
      arr.push(root.val);
      _preorderTraversal(root.left, arr);
      _preorderTraversal(root.right, arr);
    }
  }

  let arr = [];
  _preorderTraversal(root, arr);

  return arr;
}
