class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict ={}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dict:
                return[min(i, dict[diff]),max(i, dict[diff])]
            else:
                dict[nums[i]]=i
        # diff=[]
        # match = {}
        # start = 0
        # for num in nums:
        #     diff.append(target - num)
            # dict[start] = diff
            # match[start] = num
            # start++
        # i=0
        # for i in range(len(nums)):
        #     if nums[i] + diff[i] == target:
        #         return i
        #         i+=1

        # for j in nums:
        #     if nums[j] == diff[i]:
        #         return j
        # a=min(i,j)
        # b=max(i,j)
        # return a,b


            # I have something like dict = [0:4, 1:3, 2:2, 3:1],
            #  match = [0:3, 1:4, 2:5, 3:6]
            # i want to cross check the items of nums with the 
            # values in the dict

            #another method is to have nums array and a diff array 
            # such that we loop through and add corresponding
            #  element together. if equal to target, i is the 
            #  position in nums, then j is the position of diff in 
            #  nums, like maybe another loop to check through
        # for i in range(nums):
        #     if num[i] in dict.values():
        #         return i