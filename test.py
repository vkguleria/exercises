from itertools import product

if __name__=="__main__":
    A=[x for x in input().split()]
    B=[y for y in input().split()]
    #print(list(product(A,B)))
    print(*product(A,B))



