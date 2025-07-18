def isValid(s: str) -> bool:
    s_mapping = {")": "(", "]": "[", "}": "{"}
    newS = []
    for i in range(len(s)):
        if s[i] in s_mapping.values():
            newS.append(s[i])
        elif s[i] in s_mapping.keys():
            if not newS or s_mapping[s[i]] != newS.pop():
                return False

    return not newS

#try it out:
test1 = isValid("()")
print(test1)
test2 = isValid("()[]{}")
print(test2)
test3 = isValid("(]")
print(test3)
test4 = isValid("([])")
print(test4)
test5 = isValid("([)]")
print(test5)