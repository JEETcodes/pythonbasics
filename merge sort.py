def merge(list1, list2):
    """
    Merges two sorted Lists in increasing order.
    Returns: Merged List formed by merging list1 and list2.
    """
    (m, n) = (len(list1), len(list2))  # Obtaining the length of both the list
    (i, j) = (0, 0)
    merged_list = []
    while (i + j) < (m + n):
        if i == m:
            merged_list.append(list2[j])
            j = j + 1
        elif j == n:
            merged_list.append(list1[i])
            i = i + 1
        elif list1[i] < list2[j]:
            merged_list.append(list1[i])
            i = i + 1
        elif list1[i] >= list2[j]:
            merged_list.append(list2[j])
            j = j + 1
    return merged_list


def m_sort(X, start, end):
    if (end - start) <= 1:
        return X[start:end]
    else:
        mid = (start + end) // 2
    L = m_sort(X, start, mid)
    R = m_sort(X, mid, end)
    return merge(L, R)


test = [4, 36, 72, 1, 812, 4, 5, 8, 4, 23, 65, 72, 4876, 2, 5, 0, 3, 5, 3, 456, 0, 7, 6, 5, 246, 3866, 2, 8, 6, 34,
        66, ]

print(test)
print(m_sort(test, 0, len(test)))
