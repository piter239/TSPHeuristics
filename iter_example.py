import copy

s = "abc"
t = "aaebdac"

i = iter(t)

j = copy.copy(i)

if 'b' in j:
    pass

print(*j)
print(*j)
