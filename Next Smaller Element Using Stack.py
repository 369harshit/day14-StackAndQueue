def next_smaller_element_circular(nums):
    n = len(nums)
    stack = []
    result = [-1] * n

    for j in range(2):       #it means we iterate nums arr two time becs in question circular array given ie. j=0,1
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                result[stack.pop()] = nums[i]
            stack.append(i)

    return result


nums = [3,10,4,2,1,2,6,1,7,2,9]
result = next_smaller_element_circular(nums)
print("The next smaller element are:")
print(result)
