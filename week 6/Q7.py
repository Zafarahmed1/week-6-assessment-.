# Function to find the first non-repeating element in a list
def find_first_non_repeating_element(nums):
    frequency = {}  # Dictionary to store the frequency of each element

    # Count the frequency of each element in the list
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Find the first element with a frequency of 1
    for num in nums:
        if frequency[num] == 1:
            return num

    # If no non-repeating element is found, return None
    return None

# Example usage
nums = [40, 30, 40, 50, 60, 30, 50]
first_non_repeating = find_first_non_repeating_element(nums)

if first_non_repeating is not None:
    print("First non-repeating element:", first_non_repeating)
else:
    print("No non-repeating element found in the list.")