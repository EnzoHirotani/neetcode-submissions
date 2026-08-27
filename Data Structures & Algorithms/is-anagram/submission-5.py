class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        counts = {}
        countt = {}

        for letra in s:
            if letra in counts:
                counts[letra] += 1
            else:
                counts[letra] = 1

        for letra in t:
            if letra in countt:
                countt[letra] += 1
            else:
                countt[letra] = 1

        return counts == countt