wds = []
n = int(input())
for i in range(0, n):
    wds.append(input())
    
for i in range(0, len(wds)):
    word = wds[i]
    even = []
    odd = []
    for j in range(0, len(word)):
        if j % 2 == 0:
            even.append(word[j])
        else:
            odd.append(word[j])
    print(f'{"".join(even)} {"".join(odd)}')
