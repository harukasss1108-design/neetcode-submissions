class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        my_list = []
        k = 0
        for num in nums:
            if num != val:
                k=k+1
                my_list.append(num)
            else:
                continue
        nums[:] = my_list
        return k