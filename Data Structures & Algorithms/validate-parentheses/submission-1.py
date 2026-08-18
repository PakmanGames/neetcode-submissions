class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == "[" or s[i] == "{" or s[i] == "(":
                stack.append(s[i])
            elif s[i] == "]" or s[i] == "}" or s[i] == ")":
                if len(stack) <= 0:
                    return False
                curr = stack.pop()
                if curr == "[" and s[i] != "]":
                    return False
                elif curr == "{" and s[i] != "}":
                    return False
                elif curr == "(" and s[i] != ")":
                    return False
        return len(stack) == 0