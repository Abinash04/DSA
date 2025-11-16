from typing import List

class Solution(object):

    """
    Example 1:

        Input: nums = [1,0,-1,0,-2,2], target = 0
        Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    
    Example 2:

        Input: nums = [2,2,2,2,2], target = 8
        Output: [[2,2,2,2]]
    """
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort() # [-2, -1, 0, 0, 1, 2]

        final_output = []
        length = len(nums)

        for i in range(length - 3):
            fixed1 = nums[i]
            left = i + 1
            right = length - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i+1, length - 2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                fixed2 = nums[j]
                left = j+1
                right = length - 1

                while left < right:
                    output = fixed1 + fixed2 + nums[left] + nums[right]
                    if output == target:
                        final_output.append([fixed1, fixed2, nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left +=1
                        while left < right and nums[right] == nums[right+1]:
                            right -=1

                    elif output > target:
                        right -=1
                    elif output < target:
                        left +=1

        return final_output
    

sol = Solution()
input1 = [1,0,-1,0,-2,2]
input2 = [2,2,2,2,2]

print(sol.fourSum(input1, target=0))
print(sol.fourSum(input2, target=8))
