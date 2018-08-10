def fibonaci(l):

    f0 = 0
    f1 = 1
    i = 1
    alist = [f0, f1]

    while (i <= l):
        fnew = f0 + f1
        alist.append(fnew)
        f0 = f1
        f1 = fnew
        i += 1

    print (alist)
    return alist


def main_loop():
    x = fibonaci(10)
    print(x[-1], x[-2])

if __name__ == '__main__':
    main_loop()







