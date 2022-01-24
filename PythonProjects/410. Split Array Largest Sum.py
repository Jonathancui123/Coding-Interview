# is m always <= # elements?

# Brute force:
# Generate all combinations of m subarrays: O(m*n)
    # Find largest subarray sum: O(n) or O(m) with prefix sum array
# --> O(m*n^2) or O(m^2*n)


# Original: [7, 2, 5, 10, 8] 
# Prefix sum: [7, 9, 14, 24, 32]
# --> Calculate each subarray sum in O(1) time

# Suppose m = 2^x
# m=4

# Is it true, that splitting the array in half such that the sum of the left and right are as close as possible
# will lead to the minimal sum of subarrays (after any future splits)?

# if m == 1:
    # Report array sum
# Given an array, use binary search to split the array with at least floor(m/2) elements on each half
    # AND so |right half sum - left half sum| is minimized

# Call the helper on the larger sum half with ciel(m/2)
# Call the helper on the smaller sum half with floor(m/2)

# [10, 0, 6][6, 6], m=4
# [10, 0][6][6][6] --> 10

# [1, 4, 4], m=3
# [1, 4][4]
# [1][4][4] --> 4


# [1, 1, 1, 1][10, 10], m=5
# [1, 1][1, 1][10][10]
# [1, 1][1][1][10][10] --> 10

# [5, 1, 1, 10, 0, 0]


# We agree it is true that: The largest sum among subarrays is minimized, when the difference between largest sum subarray minus smallest sum subarray is minimized
# Assume that the array has been previously split to have |right half sum - left half sum| minimized
# We claim that after a new level of splitting, the difference between the largest sum subarray and the smallest sum subarray is minimized (when compared to other possible subarrays arrangements with subarrays of the same size)
# Greedy stays ahead!?

# log(n)
# log(n/2) + log(n/2)
# log(n/4) + log(n/4) + log(n/4) + log(n/4)
# => O(n^(log_2(2))) => O(n)

class Solution:
    def splitArrayHelper(self,nums, prefix_sum, left_bound, right_bound, m):
        print(nums[left_bound:right_bound+1], m)
        left_bound_sum = prefix_sum[left_bound - 1] if left_bound > 0 else 0
        if m == 1:
            return_value =  prefix_sum[right_bound] - left_bound_sum
            print("returning:", return_value)
            return return_value
            
        # leftmost element such that splitting after it will result in left side sum >= right side sum
        left = left_bound + m//2 - 1
        right = right_bound - m//2
        
        def left_sum_larger(mid):
            left_sum = prefix_sum[mid] - (prefix_sum[left_bound - 1] if left_bound > 0 else 0 )
            right_sum = prefix_sum[right_bound] - prefix_sum[mid]
            print("Check:", nums[left_bound:mid+1], nums[mid+1:right_bound+1], mid, left_sum, right_sum, left_sum >= right_sum)
            return left_sum >= right_sum

        
        while left < right:
            mid = left + (right - left)//2
            if left_sum_larger(mid):
                right = mid
            else:
                left = mid+1
        
        split = left
        left_larger = True
        if left > left_bound + m//2 - 1:
            difference1 = abs(prefix_sum[right_bound] - 2*prefix_sum[split] + left_bound_sum)
            print("difference1", difference1)
            if nums[split] < 2 * difference1:
                split = left - 1
                left_larger = False
                print("newSplit", split)
        
        if left_larger:
            left_m = (m + 1)//2
            right_m = m // 2
        else:
            left_m = m//2
            right_m = (m+1)//2
        
        left_max = self.splitArrayHelper(nums, prefix_sum, left_bound, split, left_m)
        right_max = self.splitArrayHelper(nums, prefix_sum, split + 1, right_bound, right_m)
        return max(left_max, right_max)
        
        
    
    def splitArray(self, nums: List[int], m: int) -> int:
        prefix_sum = [nums[0]]
        for num in nums[1:]:
            prefix_sum.append(num + prefix_sum[-1])
            
        return self.splitArrayHelper(nums, prefix_sum, 0, len(nums)-1, m)
        
        
        
        
        
        