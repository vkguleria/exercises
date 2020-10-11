from itertools import permutations
in_str,size=(input().split())
#l=[''.join(x) for x in permutations(sorted(in_str),int(size))]
#print("\n".join(l))
print(*[''.join(x) for x in permutations(sorted(in_str),int(size))],sep="\n")
