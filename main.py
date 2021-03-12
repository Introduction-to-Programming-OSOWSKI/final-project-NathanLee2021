def times10(n):
    return n * 10

def firstA(x):
    if x [0] == "a":
        return "True"
    else:
        return "False"

def sizer(s):
    if s < 10:
        return "small"
    elif 10 < s > 100:
            return "medium"
    else:
        return "large"

print (sizer("12"))