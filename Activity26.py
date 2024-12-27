#write a program to find the sum of natural numbers.

t=int(input("Enter the natural numbers you want to find the sum of. \n"))
sum=0
nat_count=1
while nat_count<=t:
    sum=sum+nat_count
    print("The ideration is ",nat_count)

    nat_count=nat_count+1

print("the sum is",sum)