n=int(input( ))
temp=n
reverse=0
while (n>0):
    remainder=n%10
    reverse=(reverse*10)+remainder
    n=n//10

if(temp==reverse):
    print("palindrome it is...")
else:
    print("not palindrome...")
