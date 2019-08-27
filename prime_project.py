def prime(n):
    if n==1:
        print(n,'not prime nor non-prime')
    elif n==2:
        print(n,'it is a prime')
    else:
        for i in range(2,n//2):
            if n%i==0:
                break
        else:
            print(n,'it is a prime')

start=int(input("enter a start point:"))
end=int(input("enter a end point"))
while start<=end:
    prime(start)
    start+=1
