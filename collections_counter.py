'''
Task

is a shoe shop owner. His shop has number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are number of customers who are willing to pay

amount of money only if they get the shoe of their desired size.

Your task is to compute how much money

earned.

Input Format

The first line contains
, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains , the number of customers.
The next lines contain the space separated values of the size desired by the customer and
the price of the shoe.

e.g.,:
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Output Format

Print the amount of money earned by
'''
from collections import Counter
num_shoes=int(input())
# Couter will give the {size:count} as dict for each size occuring in the list
sizes_count=Counter([ int(x) for x in input().split() ])
customers=int(input())
sale=0
for c in range(customers):
    size,cost=(int(x) for x in input().split())
    if sizes_count.get(size):
        print(f'adding {cost}')
        sale += cost
        sizes_count[size] -= 1
print(sale)
