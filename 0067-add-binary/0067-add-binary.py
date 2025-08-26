class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        res = ""
        leading = False
        i = 0

        while i < len(a) or i < len(b) or leading:
            t_a = 1 if i < len(a) and int(a[i]) else 0
            t_b = 1 if i < len(b) and int(b[i]) else 0
            lead = 1 if leading else 0

            total = t_a + t_b + lead
            if total == 2:
                res += "0"
                leading = True
            elif total == 3:
                res += "1"
                leading = True
            else:
                res += str(total)
                leading = False

            i += 1

        return res[::-1]

        