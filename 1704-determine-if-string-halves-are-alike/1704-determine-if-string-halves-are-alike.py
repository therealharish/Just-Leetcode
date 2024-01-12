class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        half = len(s)//2
        first = s[:half]
        second = s[half:]
        print(first, second)
        countFirst = 0
        countSecond = 0
        for i in first:
            if i in vowels:
                countFirst+=1
        for i in second:
            if i in vowels:
                countSecond+=1
        if countFirst == countSecond:
            return True
        else:
            return False
            