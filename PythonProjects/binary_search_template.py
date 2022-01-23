# BASED ON: 
# https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems

# Assumes monotonicity of the condition property
def binary_search(arr, target):
  def condition(mid, arr):
    return arr[mid] >= target

  left, right = 0, len(arr)-1
  # inclusive lower and upper bounds for the search
  while left < right:
    # Very important!!! Middle index must bias to the left for an even number of elements (e.g. 2 elements in search bounds, we must choose the left element as mid)
    # This is because our left bound will move to mid+1 while the right bound will not
    mid = left + (right - left)//2
    if condition(mid, arr):
      # this "binary search template" doesn't exit immediately when arr[mid] == target. 
      # Instead, the right bound will stay at the target while the left bound increases past it
      right = mid
    else:
      left = mid + 1

  # Left index will be the leftmost element that satisfies the condition (if such an element exists)
  return left if arr[left] == target else -1

print(binary_search([1,6,8,8,8,120,120,150,200], 200))