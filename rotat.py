def rotate_array(nums, k):
    """
    Rotates the array to the right by k steps in-place.
    
    Args:
    - nums: List[int] - The input array
    - k: int - The number of steps to rotate the array
    
    Returns:
    - None (modifies the input array in-place)
    """
    # If k is greater than the length of the array, take its modulo
    k = k % len(nums)

    # Reverse the entire array
    reverse(nums, 0, len(nums) - 1)
    
    # Reverse the first k elements
    reverse(nums, 0, k - 1)
    
    # Reverse the remaining elements
    reverse(nums, k, len(nums) - 1)

def reverse(nums, start, end):
    """
    Reverses the elements in the specified range of the array in-place.
    
    Args:
    - nums: List[int] - The input array
    - start: int - The starting index of the range
    - end: int - The ending index of the range
    
    Returns:
    - None (modifies the input array in-place)
    """
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

# Example Usage:
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate_array(nums, k)
print("Rotated Array:", nums)
