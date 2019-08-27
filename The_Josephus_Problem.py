def Josephus(n):
    if n % 2 == 0:
        return 1,"<= is your seat!"
    i = 1
    while 2**i < n:
        i+=1
    i-=1
    temp = n-(2**i)
    return 'you will be seating on =>',2*temp+1


print(Josephus(int(input("Enter number of people:"))))
