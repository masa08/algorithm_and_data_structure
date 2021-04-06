class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        stack = []
        for string in s:
            stack.append(string)

        for target in t:
            if stack and target == stack[0]:
                stack.pop(0)
            else:
                continue

        if not stack:
            return True
        else:
            return False


# tの中にあるs文字のindexを取得して、tをindex以降の文字列に変換する。これを最後まで繰り返す。
# もし、tのなかにsが存在しない場合は、sの並び順を満たさないことになるので例外、return Falseが返却される。
# 問題なく処理を終了した場合、is_subsequenceなことが証明されるのでreturn Trueを返す。
# class Solution:
# 	def isSubsequence(self, s: str, t: str) -> bool:
# 		for i in range(0, len(s)):
# 			try:
# 				index = t.index(s[i])
# 			except ValueError:
# 				return False

# 			t = t[index+1:]

# 		return True
