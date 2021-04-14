# TWO Pointer
# 配列操作の場合に、効率よく要素同士を比較したりして、パフォーマンス向上のために用いられるアルゴリズム
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        pointerOne = 0
        pointerTwo = 0

        while pointerOne < len(typed):
            if pointerTwo < len(name) and name[pointerTwo] == typed[pointerOne]:
                pointerTwo += 1
            # 最初の文字で一致しなかった場合はFalse
            # 文字が続いた場合、その文字は前と同じ文字であることが条件
            elif pointerOne == 0 or typed[pointerOne] != typed[pointerOne-1]:
                return False
            pointerOne += 1

        return pointerTwo == len(name)
