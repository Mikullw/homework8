def get_even(alist):
    result = []
    for a in alist:
        if a % 2 == 0:
            result.append(a)
    return result

x = [4,5,56,24,56,67,8,99,98,78,45]
print (get_even(x))