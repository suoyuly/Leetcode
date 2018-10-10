class Solution(object):

    #My stupid two sum
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum_dict = dict()
        for i in range(len(nums)):
            sum_dict[nums[i]] = i
        
        for i in range(len(nums)):
            com = target-nums[i]
            if (com in sum_dict) and (sum_dict[com] != i):
                return [i, sum_dict[com]]
        return []
		
	#elegant two sum	
	def twoSum2(self nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		sum_dict = dict()
		for i in range(len(nums)):
			n=nums[i]
			
			if (n in sum_dict) and (sum_dict[n] != i):
				return[sum_dict[n] ,i]
		
			sum_dict[target -n] = i
		return []