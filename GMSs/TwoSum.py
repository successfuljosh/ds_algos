def twoSum(nums, target):
    dict_ = {}
    for i in range(len(nums)):
        if target - nums[i] in dict_:
            return [dict_[target - nums[i]], i]
        dict_[nums[i]] = i