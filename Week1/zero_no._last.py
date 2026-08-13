nums = [0, 1, 0, 3, 12]

x = 0

for i in range(len(nums)):
    if nums[i] != 0:

        nums[x], nums[i] = nums[i], nums[x]
        x += 1
        
print(nums) 