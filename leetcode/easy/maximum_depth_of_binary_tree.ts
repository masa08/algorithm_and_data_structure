import { TreeNode } from "../common/common";

function maxDepth(root: TreeNode | null): number {
  if (root === null) {
    return null;
  }

  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
}
