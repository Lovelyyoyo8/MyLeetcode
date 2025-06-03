class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = ""

        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0:
                sum += int(a[i])
                i -= 1
            if j >= 0:
                sum += int(b[j])
                j -= 1
            result = str(sum % 2) + result
            carry = sum // 2

        if carry:
            result = '1' + result

        return result


#In Python3, convert to integer:
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1

            # Add current bit to result
            result.append(str(total % 2))
            # Update carry (0 or 1)
            carry = total // 2

        # Reverse to get correct order
        return ''.join(reversed(result))


#If not convert to integer:
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            bit_a = a[i] if i >= 0 else '0'
            bit_b = b[j] if j >= 0 else '0'

            # Convert bits manually using ASCII subtraction
            total = (ord(bit_a) - ord('0')) + (ord(bit_b) - ord('0')) + carry

            result.append('1' if total % 2 == 1 else '0')
            carry = 1 if total > 1 else 0

            i -= 1
            j -= 1

        return ''.join(reversed(result))

