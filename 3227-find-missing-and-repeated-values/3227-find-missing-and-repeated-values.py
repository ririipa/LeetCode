class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # number repeated twice lets say its a
        # number missing lets say its b
        # we required to find[a,b]
        
        # 1. we make the g rid a list 
        list = []
        for row in grid:
            for num in row:
                list.append(num)
        # 2. find a
        count = {}
        for num in list:
            count[num] = count.get(num, 0) + 1

        # 3. find b
        n = len(grid)
        total_num = set(range(1,n * n + 1))

        a, b = -1, -1

        for num in total_num:
            if num in count:
                if count[num] == 2:
                    a = num 

            else:
                b = num
        return [a,b]