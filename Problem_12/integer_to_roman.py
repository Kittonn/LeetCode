def intToroman(num):
    roman_num = [
        ["M", 1000],
        ["CM", 900],
        ["D", 500],
        ["CD", 400],
        ["C", 100],
        ["XC", 90],
        ["L", 50],
        ["XL", 40],
        ["X", 10],
        ["IX", 9],
        ["V", 5],
        ["IV", 4],
        ["I", 1],
    ]
    ans = []
    for i in roman_num:
        while num >= i[1]:
            ans.append(i[0])
            num -= i[1]

    return ''.join(ans)
