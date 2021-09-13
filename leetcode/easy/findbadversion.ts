/**
 * The knows API is defined in the parent class Relation.
 * isBadVersion(version: number): boolean {
 *     ...
 * };
 */

var solution = function (isBadVersion: any) {
  return function (n: number): number {
    let l = 0;
    let r = n - 1;

    while (l <= r) {
      let pivot = l + r; //2
      if (isBadVersion(pivot) == true) {
        r = pivot - 1;
      } else {
        l = pivot + 1;
      }
    }

    return l;
  };
};
