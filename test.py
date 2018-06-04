def get_recurring(decimals):
    if type(decimals) == float:
        decimals = str(decimals).split("0.")[1]
    options = []
    longest = 0
    for i in range(len(decimals)):
        for j in range(len(decimals[i:])):
            if decimals.count(decimals[i:j+i]) > 1:
                if decimals[i:j+i]:
                    options.append(decimals[i:j+i])
                    if len(options[-1]) > longest:
                        longest = len(options[-1])
    longest_options = []
    for i in options:
        if len(i) == longest:
            longest_options.append(i)
    if len(longest_options) == 0:
        return 0

    last_long = longest_options[-1]

    if last_long.count(last_long[0]) == len(last_long):
        return 1
    return len(last_long)

l = 0
l_l = 0
for i in range(2, 1000):
    rec = get_recurring(1/i)
    if rec > l_l:
        l_l = rec
        l = i
print(l, l_l)
