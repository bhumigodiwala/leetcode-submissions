class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Initialize maxArea as 0
        maxArea = 0

        # Create a stack which has pair of indexes and heights
        stack = [] #pair: (index, height)

        for i,h in enumerate(heights):
            start = i
            # Check if stack is not empty and 
            # if height h is less than the height at top of the stack
            # stack[-1][1] [-1] -> top of stack and [1] -> height in the pair
            while stack and stack[-1][1] > h:
                # height cannot be extended to the right so:
                # 1. pop it from the stack
                # 2. Calculate the maxArea
                # 3. the start index becomes the index at which we pop at

                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start,h))

        # If there are elements still left in the stack
        # we need to calculate maxArea with these index and heights
        for i, h in (stack):
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea