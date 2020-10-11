from itertools import product

lines,modulo = (int(x) for x in input().split())
vals = [ list(map(int, input().split()))[1:] for _ in range(lines) ]
print(vals)
results = map(lambda x: sum(i**2 for i in x)%modulo,product(*vals))
res= [ x for x in results]
print(res)
#print(*results)
print(max(res))
