class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif c == ")" or c == "}" or c == "]":
                if len(stack) <= 0:
                    return False
                curr = stack.pop()
                if curr == "(" and c != ")":
                    return False
                elif curr == "{" and c != "}":
                    return False
                elif curr == "[" and c != "]":
                    return False
        if len(stack) > 0:
            return False
        return True