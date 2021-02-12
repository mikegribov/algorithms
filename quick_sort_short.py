def quick_sort_short(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    return quick_sort_short([val for val in data if val < pivot])\
           + [val for val in data if val == pivot]\
           + quick_sort_short([val for val in data if val > pivot])