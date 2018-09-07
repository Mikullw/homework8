zhishu_list = [2, 3, 5, 7]


def main():
    for i in range(10, 200):
        flag = True
        for k in zhishu_list:
            if i % k == 0:
                flag = False
                break
        if flag:
            zhishu_list.append(i)
            print(i)
    print(zhishu_list)


def gongyinshu(x, y):
    if x < y:
        z = x
        x = y
        y = z
    while (x % y) != 0:
        c = x % y
        x = y
        y = c
    return y


if __name__ == '__main__':
    main()
