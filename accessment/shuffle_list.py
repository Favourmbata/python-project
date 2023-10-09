x = ['A', 'M', 'C', 'W', 'I''T']
v = x[::3]

print(v)

n = ['A', 'M', 'C', 'W', 'I', 'T']


def slise(s, step):
    return [s[i::step] for i in range(step)]


print(slise(n, 3))
