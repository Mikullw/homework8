
def gongyinshu(x,y):
    c = x % y
    if x < y:
        z = x
        x = y
        y = z
    while (x % y) != 0:
            x = y
            y = c
    return y

result = gongyinshu(135,7)
print (result)
