def levenshtein(a: str, b: str) -> int:
    a_len = len(a)
    b_len = len(b)

    arr = []

    """
     a_len ->
     b_len |
           v
    """

    for i in range(0, b_len + 1):
        tmp = [0 for _ in range(0, a_len + 1)]
        arr.append(tmp)

    for i in range(1, b_len + 1):
        arr[i][0] = i

    for j in range(1, a_len + 1):
        arr[0][j] = j

    for i in range(1, b_len + 1):
        for j in range(1, a_len + 1):
            if b[i - 1] == a[j - 1]:
                arr[i][j] = arr[i - 1][j - 1]
                continue
            arr[i][j] = min(arr[i - 1][j] + 1, min(arr[i][j - 1] + 1, arr[i - 1][j - 1] + 1))
    return arr[b_len][a_len]