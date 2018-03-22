# Time:  O(n)
# Space: O(1)
#
# Validate if a given string is numeric.
#
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# Note: It is intended for the problem statement to be ambiguous.
# You should gather all requirements up front before implementing one.
#

class InputType:
    INVALID    = 0
    SPACE      = 1
    SIGN       = 2
    DIGIT      = 3
    DOT        = 4
    EXPONENT   = 5


# regular expression: "^\s*[\+-]?((\d+(\.\d*)?)|\.\d+)([eE][\+-]?\d+)?\s*$"
# automata: http://images.cnitblog.com/i/627993/201405/012016243309923.png
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        transition_table = [[-1,  0,  3,  1,  2, -1],     # next states for state 0
                            [-1,  8, -1,  1,  4,  5],     # next states for state 1
                            [-1, -1, -1,  4, -1, -1],     # next states for state 2
                            [-1, -1, -1,  1,  2, -1],     # next states for state 3
                            [-1,  8, -1,  4, -1,  5],     # next states for state 4
                            [-1, -1,  6,  7, -1, -1],     # next states for state 5
                            [-1, -1, -1,  7, -1, -1],     # next states for state 6
                            [-1,  8, -1,  7, -1, -1],     # next states for state 7
                            [-1,  8, -1, -1, -1, -1]]     # next states for state 8

        state = 0
        for char in s:
            inputType = InputType.INVALID
            if char.isspace():
                inputType = InputType.SPACE;
            elif char == '+' or char == '-':
                inputType = InputType.SIGN
            elif char.isdigit():
                inputType = InputType.DIGIT
            elif char == '.':
                inputType = InputType.DOT
            elif char == 'e' or char == 'E':
                inputType = InputType.EXPONENT;

            state = transition_table[state][inputType];

            if state == -1:
                return False;

        return state == 1 or state == 4 or state == 7 or state == 8


class Solution2(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        return bool(re.match("^\s*[\+-]?((\d+(\.\d*)?)|\.\d+)([eE][\+-]?\d+)?\s*$", s))

class Solution3:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        state = [{},
                 {'blank':1, 'sign':2, 'digit':3, '.':4},
                 {'digit':3, '.':4},
                 {'digit':3, '.':5, 'e':6, 'blank':9},
                 {'digit':5},
                 {'digit':5, 'e':6, 'blank':9},
                 {'sign':7, 'digit':8},
                 {'digit':8},
                 {'digit':8, 'blank':9},
                 {'blank':9}
        ]
        currState = 1
        for c in s:
            if c >= '0' and c <= '9':
                c = 'digit'
            if c == ' ':
                c = 'blank'
            if c == '+' or c == '-':
                c = 'sign'
            if c not in state[currState].keys():
                return False
            currState = state[currState][c]
        if currState not in [3, 5, 8, 9]:
            return False
        return True

if __name__ == "__main__":
    print Solution().isNumber(" 0.1 ")
    print Solution().isNumber("abc")
    print Solution().isNumber("1 a")
    print Solution().isNumber("2e10")

