from typing import List

class Solution(object):
    """
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

    Input: nums = [0,1,1]
    Output: []

    Input: nums = [0,0,0]
    Output: [[0,0,0]]

    """
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        """
        Sort the list for 2 pointer approach:
        """
        nums.sort() # [-4,-1,-1,0,1,2]

        output = []
        length = len(nums)

        ## outer loop will go through entire list, we will keep one value fixed and use 2 pointers
        for i in range(length - 2):
            fixed = nums[i]
            left = i + 1
            right = length - 1

            # take care of duplicate entry which is already processed for outer loop.
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # iteration 1
            """
            fixed = -4, left = 1, right = 5
            """
            # inner loop
            while left < right:
                left_num = nums[left]
                right_num = nums[right]

                if fixed + left_num + right_num == 0:
                    # found the triplet, move the left towards right and right towards left.
                    output.append([fixed, nums[left], nums[right]])
                    left +=1
                    right -=1
                    while left < right and nums[left] == nums[left -1]:
                        left +=1
                        
                    while left < right and nums[right] == nums[right+1]:
                        right -=1
                        

                elif fixed + left_num + right_num > 0:
                    right -=1
                elif fixed + left_num + right_num < 0:
                    left +=1

        return output


sol = Solution()
input1 = [-1,0,1,2,-1,-4]
input2 = [0,1,1]
input3 = [0,0,0]
input4 = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
input5 = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]

print(sol.three_sum(input1))
print(sol.three_sum(input2))
print(sol.three_sum(input3))
print(sol.three_sum(input4))
print(sol.three_sum(input5))