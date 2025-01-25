class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n
        
        # Calculate left products
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]
        
        # Calculate right products and multiply with left products
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        return answer
        
        
# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4]
    print(solution.productExceptSelf(nums))  # Output: [24, 12, 8, 6]
