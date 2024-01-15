def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loseCounts = defaultdict(int)
        for lst in matches:
            loseCounts[lst[0]] += 0
            loseCounts[lst[1]] += 1
        keys = list(loseCounts.keys())
        one = list()
        two = list()
        for key in keys:
            if loseCounts[key] == 0:
                one.append(key)
            elif loseCounts[key] == 1:
                two.append(key)
        return [sorted(one), sorted(two)]