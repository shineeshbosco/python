    
n=int(input("enter a number(if 0 enter it will stop):"))
sum=0
while True:
    if (n==0):
        break
    elif (n<0):
        n=int(input("enter a number(if 0 enter it will stop):"))
        continue
    else:
        sum+=n
        print("enter of all positive numbers is :",sum)
    n=int(input("enter a number(if 0 enter it will stop):"))
print("sum of all positive numbers is :",sum)        

             