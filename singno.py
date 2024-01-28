def single_number(nums):
    """
    Finds the single number in the array where every element appears twice except for one.
    
    Args:
    - nums: List[int] - The input array
    
    Returns:
    - int: The single number
    """
    # Initialize the result to 0
    result = 0
    
    # XOR all elements in the array
    for num in nums:
        result ^= num
    
    return result

# Example Usage:
nums = [2, 3, 1, 2, 1]
print("Single Number:", single_number(nums))  # Output: 3
