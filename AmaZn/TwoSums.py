#run through a list and return indices of number that adds up to a target
#Optimized version time=O(n), space=O(n)
def twoSum(nums, target):
    visited = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in visited: #hash function here uses O(1)
            return [visited[diff], i]
        visited[nums[i]] = i

#time O(n^2), space=O(1)
def brute(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]