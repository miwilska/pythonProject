### 1. FizzBuzz:
'''
Any number divisible by three is replaced by the word fizz
and any number divisible by five by the word buzz.
Numbers divisible by 15 become fizz buzz.
'''

#   FizzBuzz my first approach:
def fizz_buzz1(until) :
    for i in range (1,until+1) :
        if i % 3 == 0 and i % 5 ==0 :
            print('FizzBuzz')
        elif i % 3 ==0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else :
            print(i)

# FizzBuzz second approach:
def fizz_buzz2(until) :
    for j in range (1,until+1) :
        n = ''
        if j % 3 == 0:
            n='Fizz'
        if j % 5 == 0:
            n = n +'Buzz'
        elif n == '' :
            n=j
        print(n)
