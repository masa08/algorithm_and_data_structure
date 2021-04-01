from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        check = []
        for i in emails:
            a = i.split('@')
            b = a[0].split('+')
            email = b[0].replace(".", "") + "@" + a[1]
            if email not in check:
                check.append(email)
        return len(check)
