def contains_duplicate(nums):
    """
    Checks if the array contains any duplicates.
    
    Args:
    - nums: List[int] - The input array
    
    Returns:
    - bool: True if any value appears at least twice, False if every element is distinct
    """
    # Create a set to store unique elements
    seen = set()

    # Iterate through the array
    for num in nums:
        # If the element is already in the set, it's a duplicate
        if num in seen:
            return True
        # Otherwise, add it to the set
        seen.add(num)

    # No duplicates found
    return False

# Example Usage:
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 3, 4, 1]

print("Array 1:", contains_duplicate(nums1))  # Output: False
print("Array 2:", contains_duplicate(nums2))  # Output: True
