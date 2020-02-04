


def maxDifference(nums):
    ans = -1
    minV = nums[0]


    for i in range(1, len(nums)):
        diffV = nums[i] - minV
        if diffV > 0 and diffV > ans:
            ans = diffV
        if minV > nums[i]:
            minV = nums[i]

    return ans

print(maxDifference([1]))
print(maxDifference([7, 1, 2, 5]))
print(maxDifference([5, 4, 3, 2, 1]))
print(maxDifference([2, 3, 10, 2, 4, 8, 1]))

