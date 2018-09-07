x = '23324545546787878765'
z = '2'

def char_in_string(a_char, a_string):
    result = False
    if a_char in a_string:
        result = True
    return result

ret = char_in_string(z, x)
print (ret)