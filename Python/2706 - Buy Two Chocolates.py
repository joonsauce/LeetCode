def buyChoco(self, prices: List[int], money: int) -> int:
    initial = 0 + money
    prices.sort()
    for i in range(2):
        money -= prices[i]
    return money if money >= 0 else initial