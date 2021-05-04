# 文字列 string を受け取り、文字数の半分を文字列の真ん中から返す、middleSubstring という関数を定義してください。（文字数が 2 以下の場合は、最初の文字を返します。）

import math


def middleSubstring(stringInput):
    if len(stringInput) <= 2:
        return stringInput[0]

    pivod = math.floor(len(stringInput) / 2)
    delete_number = math.ceil(pivod / 2)

    return stringInput[delete_number:][0:pivod]
