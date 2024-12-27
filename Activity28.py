#Write a program to check if the number entered by the user is an Armstrong number or not?

an=int(input("Enter a number. \n"))

sum=0
temp=an

while temp>0:
    digit= temp%10
    sum += digit**3
    temp //= 10

if an==sum:
    print(an," is an armsterong number.")
else:
    print(an,"is not an armstrong number.")