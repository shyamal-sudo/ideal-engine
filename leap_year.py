def leap_year(y):
    if y%100==0:
        if y%400==0:
            print(y,"It is a Leap year")
        else:
            print(y,"It is not a leap year")
    elif y%4==0:
        print(y,"It is a leap year")
    else:
        print(y,"It is not leap year")

start=int(input("enter a starting year:"))
end=int(input("enter a ending year"))
while start<=end:
    leap_year(start)
    start+=1