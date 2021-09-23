import { TreeNode } from "../common/common";

function isSymmetric(root: TreeNode | null): boolean {
  function _isSymmetric(
    first: TreeNode | null,
    second: TreeNode | null
  ): boolean {
    if (first === null && second === null) {
      return true;
    }
    if (first === null || second === null) {
      return false;
    }
    if (first.val != second.val) {
      return false;
    }
    return (
      _isSymmetric(first.left, second.right) &&
      _isSymmetric(first.right, second.left)
    );
  }

  if (root === null) return true;
  return _isSymmetric(root.left, root.right);
}
