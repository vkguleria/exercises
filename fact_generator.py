'''
works on python version 3.x
'''
import argparse,time
  
def fact(n):
    item=1    # item is the placeholder to hold the result and yield when asked for
    if n==1:
        yield 1
    while n > 1:
        item *= n
        yield item
        n -= 1

def getfact(n):
    for i in fact(n):
        pass
    return i


def main():
    parser=argparse.ArgumentParser(description='calculate the factorial of a number')
    parser.add_argument('-n','--n',required=True,type=int)
    args=parser.parse_args()
    s1=time.perf_counter()
    res=getfact(args.n)
    s2=time.perf_counter()
    print(f'result:-\n{res}\nTook {round((s2-s1),ndigits=4)}s to calculate')


if __name__=="__main__":
    main()