
def gongyinshu(x,y):
    if x < y:
        z = x
        x = y
        y = z
    while (x % y) != 0:
            c = x % y
            x = y
            y = c
    return y


num1 = int(input("请输入第一个数: "))
num2 = int(input("请输入第二个数: "))

result = gongyinshu(num1,num2)
print( num1,"和", num2,"的最大公约数为", gongyinshu(num1, num2))

