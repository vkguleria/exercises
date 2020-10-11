csize=15
c='A'

# top
for i in range(int(csize/3)):
    print((c*(i*2+1)).center(csize*2))

# middle
for i in range(i,int(csize/3)):
    print((c*(i+1)).rjust(int(csize/i))+' '.center(csize%i)+(c*(i+1)).rjust(int(csize/i)))
