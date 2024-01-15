# a DFS solution to the question
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = l1.val
        num2 = l2.val
        counter = 1
        check = l1.next
        while check is not None:
            num1 += (check.val * (10 ** counter))
            check = check.next
            counter += 1
        counter = 1
        check = l2.next
        while check is not None:
            num1 += (check.val * (10 ** counter))
            check = check.next
            counter += 1
        ans = num1 + num2
        ans = str(ans)
        if ans:
            before = ListNode(val=int(ans[0]))
            for i in range(1, len(ans)):
                new = ListNode(val=int(ans[i]), next=before)
                before = new
            return before
        return ListNode()