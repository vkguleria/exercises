'''
- The program using time-benchmarking and shows power of generators

- input from file in.txt
    Input 1 : array size
    Input 2 : array elements
- The input can be redirected from a file having two lines as the input listed above. e.g.,
        "# python progname < inputfile.txt"
- Desired Output: highest sum of contiguous subarray

- Sample O/P(with sampling of 10000 numbers):
====================:===============
     Field          :      Value
====================:===============
Max                 :         787622
Time elapsed        :         10.184
- with Generators it's halfed the time taken normally(used to be 19s w/o generators)
'''
import time

startT=time.time()    #use time() for benchmarking
rsize=int(raw_input())
arr=[int(x) for x in raw_input().split()]
#print("The input array: {0}".format(arr))
max=0
'''
***********************************************************
        getMax() - generator function for getting max
***********************************************************
'''
def getMax():
    m,start,end=0,0,0
    for i in xrange(rsize):
        sum=arr[i]
        for j in xrange(i+1,rsize):
            sum += arr[j]
            if sum > m:
                m=sum
                yield m
                start,end=i,j
'''end getMax()'''

'''
***********************************************************
        printResult() - print the result
***********************************************************
'''
def printResult(field,val):
    template="{0:<20}{1}{2:>15}".format(field,":",val)
    print(template)
''' end printResult()'''

'''
calling the generator function and store the last value of genMax() object into max
'''
for max in getMax():         # calling the generator function and store the last value of genMax() object into max
    pass

'''
print the output
'''
printResult("="*20,"="*15)
printResult(" "*5+"Field","Value"+" "*4)
printResult("="*20,"="*15)
printResult("Max",max)
printResult("Time elapsed",time.time()-startT)