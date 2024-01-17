def uniqueOccurrences(self, arr: List[int]) -> bool:
    x = set(arr)
    k = []
    for i in x:
        j = arr.count(i)
        if j in k:
            return False
        k.append(j)
    return True