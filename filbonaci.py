import datetime

MAX = 36  # not possible bigger in short time
# descirpotion http://math.uni.wroc.pl/~jagiella/p2python/skrypt_html/wyklad11.html


def fibbonaci(max):
    if max == 0:
        return 0
    f0 = 0
    f1 = 1
    for i in range(max - 1):
        f2 = f0 + f1
        f0 = f1
        f1 = f2
    return f1


start1 = datetime.datetime.now()
# for n in range(MAX):
#     print("dla ", n, ":", fibbonaci(n))
aa = fibbonaci(MAX)
duration1 = datetime.datetime.now() - start1
print('dla', MAX, ': ', aa)
print('program tylko wartości trwał:', duration1)
print('***********************')


def fibonaci_rek(max):
    if max == 0:
        return 0
    if max == 1:
        return 1
    if max > 1:
        return fibonaci_rek(max - 1) + fibonaci_rek(max - 2)


start2 = datetime.datetime.now()
# for n in range(MAX):
#     print("dla ", n, ":", fibonaci_rek(n))
bb = fibonaci_rek(MAX)
duration2 = datetime.datetime.now() - start2
print('program rekurencja trwał:', duration2)
print('dla', MAX, ': ', bb)
print('***********************')


# Fibonacci series: (from https://docs.python.org/3/tutorial/introduction.html#strings)
# the sum of two elements defines the next
def other_fib(n):
    a, b = 0, 1
    iteration = 0
    while iteration < n:
        a, b = b, a + b
        iteration += 1
    return a


start3 = datetime.datetime.now()
# for n in range(MAX):
#     print("dla ", n, ":", fibonaci_rek(n))
cc = other_fib(MAX)
duration3 = datetime.datetime.now() - start3
print('program ze strony trwał:', duration3)
print('dla', MAX, ': ', cc)
print('***********************')

# inne wersje : https://ufkapano.github.io/algorytmy/lekcja08/dynamic.html

# http://math.uni.wroc.pl/~jagiella/p2python/skrypt_html/wyklad11.html
# "cache", albo "schowek", początkowo stowarzyszający 0 i 1 z fib(0) i fib(1) odpowiednio.
# trzymanie cache w globalnym bloku to wspomniana wyżej wada
cache = {0: 0, 1: 1}

def fib_cache(n):
    if n not in cache: # wartość fib(n) jeszcze nie zapamiętana w schowku? Liczmy ją więc:
        cache[n] = fib_cache(n - 1) + fib_cache(n - 2)
    return cache[n]  # zwracamy wartość odczytaną ze schowka


start4 = datetime.datetime.now()
# for n in range(MAX):
#     print("dla ", n, ":", fibonaci_rek(n))
dd = fib_cache(MAX)
duration4 = datetime.datetime.now() - start4
print('program rek z cache trwał:', duration4)
print('dla', MAX, ': ', dd)
print('***********************')


def fib_cache2(n, cache2=[0, 1]):
    for _ in range(n - len(cache2) + 1):
        cache2.append(cache2[-1] + cache2[-2])
    return cache2[n]


start5 = datetime.datetime.now()
# for n in range(MAX):
#     print("dla ", n, ":", fibonaci_rek(n))
ee = fib_cache2(MAX)
duration5 = datetime.datetime.now() - start5
print('program rek z cache2 trwał:', duration5)
print('dla', MAX, ': ', ee)
print('\n\n **************************\n\n')



# fill in this function
def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b


# testing code
import types

if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break