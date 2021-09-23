import { TreeNode } from "../common/common";

function postorderTraversal(root: TreeNode | null): number[] {
  function _postorderTraversal(root: TreeNode | null, arr: number[]): void {
    if (root != null) {
      _postorderTraversal(root.left, arr);
      _postorderTraversal(root.right, arr);
      arr.push(root.val);
    }
  }

  let arr = [];
  _postorderTraversal(root, arr);

  return arr;
}
