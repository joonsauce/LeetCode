def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    nums = 0
    returns = deque()
    if low <= root.val <= high:
        nums += root.val
    check = root.left
    while check is not None:
        if low <= check.val <= high:
            nums += check.val
        if check.right is not None:
            returns.append(check.right)
        check = check.left
    check = root.right
    while check is not None:
        if low <= check.val <= high:
            nums += check.val
        if check.left is not None:
            returns.append(check.left)
        check = check.right
    while returns:
        for i in range(len(returns)):
            k = returns.pop()
            if low <= k.val <= high:
                nums += k.val
            if k.left is not None:
                returns.append(k.left)
            if k.right is not None:
                returns.append(k.right)
    return nums