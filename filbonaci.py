import datetime
MAX = 35


def fibbonaci(max):
    if max == 0:
        return 0
    f0 = 0
    f1 = 1
    for i in range(max-1):
        f2 = f0 + f1
        f0 = f1
        f1 = f2
    return f1


start = datetime.datetime.now()
# for n in range(MAX):
#     print("dla ", n, ":", fibbonaci(n))
aa = fibbonaci(MAX)
duration = datetime.datetime.now() - start
print('dla', MAX, ': ', aa)
print('program trwał:', duration)
print('***********************')


def fibonaci_rek(max):
    if max == 0:
        return 0
    if max == 1:
        return 1
    if max >1:
        return fibonaci_rek(max-1)+fibonaci_rek(max-2)

start = datetime.datetime.now()
# for n in range(MAX):
#     print("dla ", n, ":", fibonaci_rek(n))
bb= fibonaci_rek(MAX)
duration = datetime.datetime.now() - start
print('program trwał:', duration)
print('dla', MAX, ': ', bb)
