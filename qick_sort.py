def quick_sort(data, left, right):
    def get_pivote(data, left, right):
        # select middle value from left, right and middle elements
        # on average, 2.5 comparisons
        index = (left + right) // 2
        l = data[left]
        r = data[right]
        m = data[index]
        if m == r:
            return m
        elif m < r:
            if l == m:
                return m
            elif l < m:
                return m
            else:
                if l < r:
                    return l
                else:
                    return r
        else:
            if l == r:
                return l
            elif l < r:
                return r
            else:
                if l < m:
                    return l
                else:
                    return m

    def get_partition(data, left, right):
        pivot = get_pivote(data, left, right)

        while left <= right:
            while data[left] < pivot:
                left += 1
            while data[right] > pivot:
                right -= 1

            if left <= right:
                data[left], data[right] = data[right], data[left]
                left += 1
                right -= 1

        return left

    if left >= right:
        return

    pivot_index = get_partition(data, left, right)
    quick_sort(data, left, pivot_index - 1)
    quick_sort(data, pivot_index, right)
