''' Program to find DayOfweek from given date. We Use zeller's algorithm to find it.
The formula is
 h = q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j
 where,
        *h is the day of week given as (0:saturday,1:sunday,2:monday an so on)
        *q is the day of month
        *m is the month starting from 3:march, 4:April, 5:May ..... 12:December.(January and february are counted as
        months 13 and 14 of the previous year) 
        *j is century (year//100)
        *k is the year of the century (year%100)'''

days = ("Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday")


def dayOFweek(day, month, year) :
    #Jan is consider as 13th month for this algorithm 
    if (month == 1): 
        month = 13
        year = year - 1
    #Feb is consider as 14th month for this algorith
    if (month == 2): 
        month = 14
        year = year - 1
    q = day 
    m = month 
    k = year % 100 
    j = year // 100
    #zellers formula
    h = q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j 
    h = h % 7
    print(days[h]) 


def main():
    day =int(input("Enter the day of month:"))
    month = int(input("Enter Month No.: "))
    year = int(input("Enter Year: "))
    dayOFweek(day,month,year)


main()
