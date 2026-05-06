class Solution:
    def isValid(self, s: str) -> bool:
        stack :str = []
        for character in s:
            if character in "({[":
                stack.append(character)
            elif character == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif character == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif character == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False