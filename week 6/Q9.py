# Function to find a triplet with a given sum in a list
def find_triplet_with_sum(nums, target_sum):
    n = len(nums)

    # Sort the list for efficient checking of triplets
    nums.sort()

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target_sum:
                return [nums[i], nums[left], nums[right]]
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1

    return None  # No triplet found

# Example usage
nums = [10, 20, 30, 9]
target_sum = 59

triplet = find_triplet_with_sum(nums, target_sum)

if triplet:
    print("Triplet with sum", target_sum, ":", triplet)
else:
    print("No triplet found with sum", target_sum)