def two_sum(num, target):
    ans = []
    for i in range(len(num)):
        for j in range(i):
            if num[i] + num[j] == target:
                ans.append(i)
                ans.append(j)
    return sorted(ans)
