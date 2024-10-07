target = 9
nums = [2, 7, 11, 15]


# for n in nums:
#     if target - n in nums:
#         print([nums.index(n), nums.index(target - n)])
#         break

class soluation(object):
    def twosum(self, nums: list, target: int):

        number_map = {}
        # print(number_map)

        for i, num in enumerate(nums):
            diff = target - num

            if diff in number_map:
                return [i, number_map[diff]]
            
            number_map[num] = i

        return None
    
s = soluation()
print(s.twosum(nums, target))

target = 6
nums = [3, 2, 4]

s1 = soluation()
print(s1.twosum(nums, target))


