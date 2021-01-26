class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i in range(len(l)):
#             Iterate through each query
            queryLen = abs(l[i] - r[i]) + 1
            if (queryLen < 2):
                result.append(False)
                continue
            querySet = set()
            duplicatesFound = False
            smallest = nums[l[i]] if nums[l[i]] < nums[l[i] + 1] else nums[l[i] + 1]
            secSmallest = nums[l[i] + 1] if nums[l[i]] < nums[l[i] + 1] else nums[l[i]]
            for numIndex in range(l[i], r[i] + 1):
#               populate the set of numbers in the query
#               also find the smallest and second smallest numbers
                if nums[numIndex] in querySet:
                    duplicatesFound = True
                else:
                    querySet.add(nums[numIndex])
                
                if numIndex >= l[i] + 2:
                    candidate = nums[numIndex]
                    if candidate < smallest:
                        secSmallest = smallest
                        smallest = candidate
                    elif candidate < secSmallest:
                        secSmallest = candidate
                
            if len(querySet) == 1:
                result.append(True)
                continue
            if duplicatesFound == True:
                result.append(False)
                continue
#               we had duplicate numbers when we needed a sequence of unique numbers
            
            difference = secSmallest - smallest
            for j in range(queryLen):                                             
                if smallest + (j * difference) not in querySet:
                    result.append(False)
                    break
            else:
                result.append(True)
        return result