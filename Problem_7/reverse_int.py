def reverse_int(x):
    ans = 0
    if x < 0:
        x *= -1
        ans = int("-"+str(x)[::-1])
    else:
        ans = int(str(x)[::-1])

    if ans < pow(-2, 31) or ans > pow(2, 31)-1:
        return 0
    return ans
