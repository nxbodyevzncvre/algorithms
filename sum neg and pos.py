def count_positives_sum_negatives(arr):
    positive = 0
    negative = 0
    neitral = 0
    size = len(arr)
    if not arr:
        return []
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += i
        elif size == 0:
            positive, negative = 0, 0
    return [positive, negative]
