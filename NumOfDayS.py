
daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):

    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def Count_Days(year1, month1, day1):
    if month1 ==2:
        if isLeapYear(year1):
            if day1 < daysOfMonths[month1-1]+1:
                return year1, month1, day1+1
            else:
                if month1 ==12:
                    return year1+1,1,1
                else:
                    return year1, month1 +1 , 1
        else: 
            if day1 < daysOfMonths[month1-1]:
                return year1, month1, day1+1
            else:
                if month1 ==12:
                    return year1+1,1,1
                else:
                    return year1, month1 +1 , 1
    else:
        if day1 < daysOfMonths[month1-1]:
             return year1, month1, day1+1
        else:
            if month1 ==12:
                return year1+1,1,1
            else:
                return year1, month1 +1 , 1


def daysBetweenDates(y1, m1, d1, y2, m2, d2):

    if y1 > y2:
        m1,m2 = m2,m1
        y1,y2 = y2,y1
        d1,d2 = d2,d1
    days=0
    while(not(m1==m2 and y1==y2 and d1==d2)):
        y1,m1,d1 = Count_Days(y1,m1,d1)
        days+=1
    return days

def main():
    Start_year = int(input("Enter Your birth year: "))
    Start_month = int(input("Enter Your birth month: "))
    Start_dayOfMonth = int(input("Enter Your birth dayOfMonth: "))

    currernt_year = int(input("Enter  current year: "))
    curernt_month = int(input("Enter  current month: "))
    current_dayOfMonth = int(input("Enter current dayOfMonth: "))

    print(daysBetweenDates(Start_year,Start_month,Start_dayOfMonth,currernt_year,curernt_month,current_dayOfMonth))

main()