"""
Using DFA, change state when get a string.

"""

class State(object):
    def __init__(self, accept, final, next_state):
        self.accept = accept
        self.final = final
        self.next_state = next_state

class Solution(object):
    nums = [str(n) for n in range(10)]
    e = ['e']
    dot = ['.']
    sign = ['+', '-']
    s_map = {
        'START': State([sign, nums, dot], 0, ['SIGN', 'INT', 'DOT']),
        'INT': State([nums, e, dot], 1, ['INT', 'E', 'DOTT']),
        'SIGN': State([nums, dot], 0, ['INT', 'DOT']),
        'E': State([nums, sign], 0, ['EN', 'ENS']),
        'EN': State([nums], 1, ['EN']),
        'ENS': State([nums], 0, ['EN']),
        'DOT': State([nums], 0, ['DEC']),
        'DOTT': State([nums, e], 1, ['DEC','E']),
        'DEC': State([nums, e], 1, ['DEC', 'E'])
        
    }
    
    def solve(self, state, i):
        if i == self.len:
            return True if state.final else False
        c = self.s[i]
        for j, v in enumerate(state.accept):
            if c in v:
                return self.solve(self.s_map[state.next_state[j]], i+1)
        return False
        
            
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        self.s = s.lstrip().rstrip()
        self.len = len(self.s)
        return self.solve(self.s_map['START'], i)