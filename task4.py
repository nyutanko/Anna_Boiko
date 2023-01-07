def count_how_many_pairs_give_sum_eq_target(array, target: int):
    result: int = 0
    for i in range(len(array)):
        val_to_find = target - array[i]
        result += array[i:].count(val_to_find)
    return result

print(count_how_many_pairs_give_sum_eq_target([1, 3, 6, 2, 2, 0, 4, 5], 5))
