print('\t\tWELCOME TO THE 13 NUMBER GAME')
print('**RULES**')
print('You can enter numbers between 1-3')
add=0
total=13
while True:
    if total==1:
        print('i won')
        break
    num=int(input("enter your number:"))

    if num<=3:
        if num+1 == 4:
            print('My number is 1')
            add=num+1
            total=total-add
            print('total is: ',add)
        elif num+2==4:
            print('My number is 2')
            add=num+2
            total=total-add
            print('total is: ',add)
        elif num+3==4:
            print('My number is 3')
            add=num+3
            total=total-add
            print('total is: ',add)
    else:
        print('Hey! Are you serious=>" DO NOT CHEAT"')
        break