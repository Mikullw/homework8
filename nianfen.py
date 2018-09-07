def LeapYear(year):
    flag = False
    if (year%4==0) and (year%100>0) or (year%400==0):
        flag=True
    return flag

def main (year,month,date):
    days_month_list = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    day = 0
    #x = year
    #y = month
    #z = date
    flag = LeapYear(year)
    if flag :
        days_month_list[2] += 1

    else:
         day = day + 1
         a = month - 1
    for i in range(month-1,0,-1):
        if ( i == 11) or (i == 9) or (i == 6) or (i == 4):
            day = day + 30
        else:
            if i == 2 :
                day = day + 28
            else:
                day = day + 31
        #a = a - 1

    day = day + z

    return day


x = int(input("年: "))
y = int(input("月: "))
z = int(input("日: "))


if __name__ == '__main__':
    result = main(x,y,z)
    print ("您输入的日期是这年的第" + str(result) + "天")
