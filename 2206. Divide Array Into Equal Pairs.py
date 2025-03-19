class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # divide nums in n pair
        # exactly one pair
        # elements present in pair has to be same
        # if all above, return true else false 
# creating map
        ok = {}

        # looping thrugh one by one 
        for num in nums:
            if num in ok:
                ok[num] += 1

            else:
                ok[num] = 1

        # check counts are even
        for count in ok.values():
            if count % 2 != 0:
             return False

        return True

