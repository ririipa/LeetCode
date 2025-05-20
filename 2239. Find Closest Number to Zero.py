class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:

        closest = nums[0] #starting with frist number(?)

        for num in nums:
            if (num < 0 ):
                num_distance = num * -1
            else:
                num_distance = num

            if (closest < 0):
                closest_distance = closest * -1
            else:
                closest_distance = closest
            if num_distance < closest_distance:
                closest = num

            elif num_distance == closest_distance and num > closest:
                closest = num
        return closest