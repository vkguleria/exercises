import subprocess as sp

def ipcheck(pop):
    status,result = sp.getstatusoutput("ping -c1 " + str(pop))
    if status == 0:
        print("System " + str(pop) + " is UP !")
    else:
        print("System " + str(pop) + " is DOWN !")


#pop = input("Enter the ip address: ")
for ip in ['8.8.8.8', '8.8.4.4', '192.168.1.1']:
    ipcheck(ip)

