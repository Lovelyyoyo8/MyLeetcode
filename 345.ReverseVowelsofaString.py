class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)  # Convert string to a list to modify it
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer to the next vowel
            while left < right and s[left] not in vowels:
                left += 1
            # Move right pointer to the previous vowel
            while left < right and s[right] not in vowels:
                right -= 1
            
            # Swap the vowels at left and right pointers
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return "".join(s)  # Convert list back to string
