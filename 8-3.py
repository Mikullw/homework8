def count(a_char, a_string):
    result = 0
    for a in a_string:
        if a == a_char:
            result = result + 1
    return result


x = '23324545546787878765'
z = '7'

ret = count(z, x)
print (ret)