import timeit
import numpy as np
import copy
import random

# https://analityk.edu.pl/kopiowanie-list-i-slownikow/

num_iter_big = 1_000_000
num_iter_small = 100


def calculate_time_of_copy(num_iter, element, name):
    print("\n Statistics of copy different methods: " + name + " of :" + str(num_iter) + ' iteration\n')
    import copy
    list_to_copy = element
    czas1 = timeit.timeit(stmt="""copied_list=[item for item in list_to_copy]""", globals=locals(), number=num_iter)
    czas2 = timeit.timeit(stmt="""copied_list=copy.deepcopy(list_to_copy)""", globals=locals(), number=num_iter)
    czas3 = timeit.timeit(stmt="""copied_list=list_to_copy[0:len(list_to_copy)]""", globals=locals(), number=num_iter)
    czas4 = timeit.timeit(stmt="""copied_list=copy.copy(list_to_copy)""", globals=locals(), number=num_iter)
    czas5 = timeit.timeit(stmt="""copied_list=list_to_copy[:]""", globals=locals(), number=num_iter)
    czas6 = timeit.timeit(stmt="""copied_list=[*list_to_copy]""", globals=locals(), number=num_iter)
    czas7 = timeit.timeit(stmt="""copied_list=list_to_copy*1""", globals=locals(), number=num_iter)
    copied_list = []
    czas8 = timeit.timeit(stmt="""for item in list_to_copy: copied_list.append(item)""", globals=locals(),
                          number=num_iter)
    czas9 = timeit.timeit(stmt="""copied_list=list(list_to_copy)""", globals=locals(), number=num_iter)
    czas10 = timeit.timeit(stmt="""copied_list=[]; copied_list.extend(list_to_copy)""", globals=locals(),
                           number=num_iter)
    # czas11 = timeit.timeit(stmt="""copied_list=list_to_copy.copy()""", globals=locals(), number=num_iter)
    # czas12 = timeit.timeit(stmt="""copied_list=np.copy(list_to_copy)""", globals=locals(), number=num_iter)
    # czas13 = timeit.timeit(stmt="""copied_list=np.array([*list_to_copy])""", globals=locals(), number=num_iter)

    wyniki = [["List comprehension =>", czas1], ["copy.deepcopy() =>", czas2], ["[0:len(numbers)] =>", czas3],
              ["copy.copy() =>", czas4], ["[:] =>", czas5], ["*args =>", czas6], ["*1 =>", czas7],
              ["Plain loop  =>", czas8], ["Conversion list() =>", czas9], ["extend() =>", czas10]
              # , ["Build-in copy() =>", czas11], ["np.copy =>", czas12], ["*args =>", czas13]
              ]

    [print(wynik[0], wynik[1]) for wynik in sorted(wyniki, key=lambda x: x[1])]

    print('**********************************************************************************')
    return wyniki


calculate_time_of_copy(num_iter_big, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], "simple list")

calculate_time_of_copy(num_iter_small, random.sample(range(7_000_000), 1_000_000), "random sample")

calculate_time_of_copy(num_iter_small, np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9]]), "simple numpy array")

calculate_time_of_copy(num_iter_small, np.array([random.sample(range(7_000_000), 1_000_000)]), "random numpy array")


def calculate_time_of_copy2(num_iter, element, name):
    print("\n Statistics of copy different methods: " + name + " of :" + str(num_iter) + ' iteration\n')
    arr = element
    import copy
    import numpy as np
    czas1 = timeit.timeit(stmt="""arr2=np.array([item for item in arr])""", globals=locals(), number=num_iter)
    czas2 = timeit.timeit(stmt="""arr2=copy.deepcopy(arr)""", globals=locals(), number=num_iter)
    czas3 = timeit.timeit(stmt="""arr2=arr[0:len(arr)]""", globals=locals(), number=num_iter)
    czas4 = timeit.timeit(stmt="""arr2=copy.copy(arr)""", globals=locals(), number=num_iter)
    czas5 = timeit.timeit(stmt="""arr2=arr[:]""", globals=locals(), number=num_iter)
    czas6 = timeit.timeit(stmt="""arr2=np.array([*arr])""", globals=locals(), number=num_iter)
    czas7 = timeit.timeit(stmt="""arr2=arr*1""", globals=locals(), number=num_iter)
    # czas8=timeit.timeit(stmt="""arr2=[]; for item in arr: arr2.append(item)""", globals=locals(), number=num_iter)
    czas9 = timeit.timeit(stmt="""arr2=np.array(arr)""", globals=locals(), number=num_iter)
    # czas10=timeit.timeit(stmt="""arr2=[]; arr2.extend(arr)""", globals=locals(), number=num_iter)
    czas11 = timeit.timeit(stmt="""arr2=arr.copy()""", globals=locals(), number=num_iter)
    czas12 = timeit.timeit(stmt="""arr2=np.copy(arr)""", globals=locals(), number=num_iter)

    wyniki = [["List comprehension =>", czas1], ["copy.deepcopy() =>", czas2], ["[0:len(numbers)] =>", czas3],
              ["copy.copy() =>", czas3], ["[:] =>", czas5], ["*args =>", czas6], ["*1 =>", czas7],
              ["Konwersja =>", czas9], ["Wbudowane copy() =>", czas11], ["np.copy =>", czas12]]

    [print(wynik[0], wynik[1]) for wynik in sorted(wyniki, key=lambda x: x[1])]


calculate_time_of_copy2(num_iter_small, np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9]]), "simple array")

calculate_time_of_copy2(num_iter_small, np.array([random.sample(range(7_000_000), 1_000_000)]), "random array")
