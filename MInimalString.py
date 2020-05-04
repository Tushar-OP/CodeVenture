s = input()
a = [0]*26
for i in s:
    a[ord(i)-97] += 1
t, u = [], []
for i in s:
    t.append(i)
    a[ord(i)-97] -= 1
    while t and sum(a[:ord(t[-1])-97]) == 0:
        u.append(t.pop())
print(''.join(u))
