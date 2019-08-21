# pythonbasics
Basic Python codes intended for beginners.
def m_sort(X, start, end):
    if (end - start) <= 1:
        return X[start:end]
    else:
        mid = (start + end) // 2
    L = m_sort(X, start, mid)
    R = m_sort(X, mid, end)
    return merge(L, R)
