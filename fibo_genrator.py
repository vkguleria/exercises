'''
Output will be fibonacci series: 0 1 1 2 3 5 8 .....

'''

import argparse,time

def fibo(n):
    a,b=0,1
    if n==1:
        yield a
    while n > 0:
        yield a
        a,b = b,a+b
        n -= 1



def main():
    parser=argparse.ArgumentParser(description='Fibonacci series upto a desires number of times')
    parser.add_argument('-n','--n',required=True,type=int)
    args=parser.parse_args()
    num=args.n
    s1=time.perf_counter()
    for i in fibo(num):
        print(f'{i}',end=' ')
    s2=time.perf_counter()
    print(f'\nTook {round((s2-s1),ndigits=4)}s')

if __name__ == "__main__":
    main()
