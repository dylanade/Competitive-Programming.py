class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # stack = []
        # for i in range(len(a)):
        ## > monotonic increasing stack
        ## < monotonic decreasing stack
        #     while stack and stack[-1] > a[i]:
        #         stack.pop()
        #     stack.append(a[i])
        # print(stack)
        
        
        mp = {num : -1 for num in nums1}
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                top = stack.pop()
                if top in mp:
                    mp[top] = num
            stack.append(num)
        return list(mp.values())
        