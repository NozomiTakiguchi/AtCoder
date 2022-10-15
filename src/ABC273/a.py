f = []
f.append(1)
for i in range(1,11):
    f.append(i*f[i-1])

print(f[int(input())])