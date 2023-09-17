def has_sublist_with_zero_sum(nums):
    sum_set = set()
    cumulative_sum = 0

    for num in nums:
        cumulative_sum += num


        if cumulative_sum == 0 or cumulative_sum in sum_set:
            return True

        sum_set.add(cumulative_sum)


    return False


nums = [40, 20, -30, 10, 50]
result = has_sublist_with_zero_sum(nums)

if result:
    print("There is a sub-list with a sum equal to zero.")
else:
    print("There is no sub-list with a sum equal to zero.")