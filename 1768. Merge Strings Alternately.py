class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # inatial the var
        p1 = 0
        p2 = 0
        x = len(word1)
        y = len(word2)

        answer = ''
        while p1 < x or p2 < y:
            if p1 < x:
                answer = answer + word1[p1]
                p1 += 1
            if p2 < y:
                answer = answer + word2[p2]
                p2 += 1

        return answer


