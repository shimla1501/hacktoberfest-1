n=int(input("Enter any number"))
a=n
rev=0
while n>0:
    rev=rev*10+n%10
    n=n//10
if rev==a:
    print("Palindrome")
else:
    print("Not palindrome")
    
