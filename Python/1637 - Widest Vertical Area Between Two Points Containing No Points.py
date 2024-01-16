# both solutions take similar time and memory
def maxWidthOfVerticalArea(self, points):
    x = sorted([i[0] for i in points])
    diff = []
    for i in range(len(x) - 1):
        diff.append(abs(x[i] - x[i+1]))
    return max(diff)

'''
def maxWidthOfVerticalArea(self, points):
    x = sorted([i[0] for i in points])
    diff = deque()
    for i in range(len(x) - 1):
        diff.append(abs(x[i] - x[i+1]))
    return max(diff)
'''