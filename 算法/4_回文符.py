def is_check(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_check(s[1:-1])


S = input("")
print(is_check(S))
