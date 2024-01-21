def isAcronym(self, words: List[str], s: str) -> bool:
    new = [i[0] for i in words]
    new_s = ''.join(new)
    return new_s == s