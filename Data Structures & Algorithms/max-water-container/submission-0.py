class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        low = 0
        high = n - 1
        mArea = -1
        while low < high:
            lowBar = heights[low]
            highBar = heights[high]
            cArea = (high - low) * min(lowBar, highBar)
            mArea = max(cArea, mArea)
            if highBar >= lowBar:
                low += 1
            else:
                high -= 1
        
        return mArea

        