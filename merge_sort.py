def merge(data1, data2):
    pos1 = pos2 = 0
    len1, len2 = len(data1), len(data2)
    result = []
    while pos1 < len1 and pos2 < len2:
        v1, v2 = data1[pos1], data2[pos2]
        if v1 < v2:
            result.append(v1)
            pos1 += 1
        else:
            result.append(v2)
            pos2 += 1

    return result + data1[pos1:] + data2[pos2:]


def merge_sort(data):
    len_data = len(data)
    if len_data == 1:
        return data
    else:
        half_len_data = len_data // 2
        left_data = merge_sort(data[:half_len_data])
        right_data = merge_sort(data[half_len_data:])
        return merge(left_data, right_data)