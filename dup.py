def remove_duplicates(nums):
    """
    Removes duplicates from a sorted array in-place.
    
    Args:
    - nums: List[int] - The sorted array
    
    Returns:
    - int: The new length of the array after removing duplicates
    """
    # Edge case: If the array is empty, no duplicates to remove
    if not nums:
        return 0

    # Initialize a pointer to keep track of the unique elements
    unique_pointer = 0

    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # If the current element is different from the previous unique element
        if nums[i] != nums[unique_pointer]:
            # Move the unique pointer forward
            unique_pointer += 1
            # Update the unique element at the new position
            nums[unique_pointer] = nums[i]

    # The length of the array with unique elements is (unique_pointer + 1)
    # Return this length and the modified array is already in-place
    return unique_pointer + 1

# Example Usage:
nums = [1, 1, 2, 2, 3, 4, 4, 4, 5,6,7,7,8]
new_length = remove_duplicates(nums)
print(f"Original Array: {nums[:new_length]}")
print(f"New Length: {new_length}")
