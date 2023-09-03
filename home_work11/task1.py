def pair_sum(numbers, target_sum):
    num_index = {}
    for i, num in enumerate(numbers):

        complement = target_sum - num

        if complement in num_index:
            return True

        num_index[num] = i

    return False


numbers1 = [1, 2, 3, 4, 5]
target_sum1 = 9
print(pair_sum(numbers1, target_sum1))

numbers2 = [6, 7, 8, 9, 10]
target_sum2 = 20
print(pair_sum(numbers2, target_sum2))
