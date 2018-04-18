# Time:  O(n)
# Space: O(1)
#
# You are given two linked lists representing two non-negative numbers.
<<<<<<< HEAD
# The digits are stored in reverse order and each of their nodes contain a single digit.
=======
# The digits are stored in reverse order and each of their nodes contain
# a single digit.
>>>>>>> 5efab83f5470530a2029f4839530ae1535bf1f22
# Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

<<<<<<< HEAD
class Solution3(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        """
        dummy = tmp = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            a, b = 0, 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            su = a + b + carry
            tmp.next = ListNode(su%10)
            carry = su//10
            tmp = tmp.next
        return dummy.next
=======

>>>>>>> 5efab83f5470530a2029f4839530ae1535bf1f22
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current, carry = dummy, 0

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            current.next = ListNode(val)
            current = current.next

        if carry == 1:
            current.next = ListNode(1)

        return dummy.next
<<<<<<< HEAD

if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    result = Solution().addTwoNumbers(a, b)
    print "{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val)

=======
>>>>>>> 5efab83f5470530a2029f4839530ae1535bf1f22
