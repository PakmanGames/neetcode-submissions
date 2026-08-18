class Solution:
    def isValid(self, s: str) -> bool:
        chars = list(s)
        stack = []
        for i in range(len(chars)):
            if chars[i] == "[" or chars[i] == "(" or chars[i] == "{":
                stack.append(chars[i])
            elif chars[i] == "]" or chars[i] == ")" or chars[i] == "}":
                if len(stack) <= 0:
                    return False
                curr = stack.pop()
                if curr == "[" and chars[i] != "]":
                    return False
                elif curr == "(" and chars[i] != ")":
                    return False
                elif curr == "{" and chars[i] != "}":
                    return False
        if len(stack) > 0:
            return False
        return True