class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Approach 1: Merge Sort
        # O(m+n) time and O(1) space

        # m, n = len(nums1), len(nums2)
        # p1, p2 = 0, 0

        # if p1 < m and p2 < n:
        #     if nums[p1] < nums[p2]:


        # Approach 2: Binary Search
        # O(log(min(m,n))) time

        A, B = nums1, nums2
        # Total length of merged array
        total = len(nums1) + len(nums2)
        # half length
        half = total // 2 # // used for integer division 

        # Check that we do binary search on smaller aaray
        if len(B) < len(A):
            A, B = B, A

        # Run binary search on A because A is smaller array
        l, r = 0, len(A) - 1

        while True:
            # compute mid of array A
            i = (l+r)//2

            # pointer for B
            # j -> index of mid element of array B
            # additionaly subtract 2 from half - i because arrays are 0 - indexed also j and i both start as 0 so -2
            # it will avoid errors due to indexing
            j = half - i - 2 

            # To avoid avoid out of bounds for indexes use if conditions below

            Aleft = A[i] if i >= 0 else float('-infinity')                #mid / last ele of left part of A
            Aright = A[i+1] if (i+1) < len(A) else float('infinity')      #mid+1 / first ele of right part of A

            Bleft = B[j] if j >= 0 else float('-infinity')                 #mid / last ele of left part of B
            Bright = B[j+1] if (j+1) < len(B) else float('infinity')      #mid+1 / first ele of right part of B

            # Check if the partitions are correct
            if Aleft <= Bright and Bleft <= Aright:
                # This means our left partition of B is correct
                
                # Case 1: odd no of elements
                if total % 2:
                    return min(Aright, Bright)
                # Case 2: even no of elements
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                # This means too many elements from A so reduce size(A)
                r =  i - 1

            else:
                # This means left partion of A is smaller so we increase left part of A
                l = i + 1



            

                
        