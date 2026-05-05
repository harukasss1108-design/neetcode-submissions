class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_value = arr[len(arr)-1]
        for i in range(len(arr)-2,-1,-1):
            current_value = arr[i]
            arr[i] = max_value
            if current_value>max_value:
                max_value = current_value

        arr[len(arr)-1]=-1

        return arr
                


