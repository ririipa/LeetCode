class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # merging the lists 
        list = nums1 + nums2
        
        # sort by the id
        list.sort()


        # creating empty list 
        result= []

        # loop through the list
        for id, val in list: 
            # last added id same, sum the values
            if result and result[-1][0] == id: 
                result[-1][1] += val   # Add to the  Value NOT  (to the id) 

        # if new id then add the new pair  yayy
            else:
                result.append([id, val])

        return result





        
        