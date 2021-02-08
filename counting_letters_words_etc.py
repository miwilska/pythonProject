### 3. Counting words, letters etc .
#Make function to counting words, letters and frequency of letters in string


#   Counting words, letters etc  my first approach:
my_first_text = 'Ala ma kota, a kot ma Ale'

def counting_function1(text) :
    words = 1
    letters =0
    hash_table = {}
    for t in text :
        if t == ' ' :
            words += 1
        else :
            t = t.lower()
            letters +=1
            if t in hash_table :
                hash_table[t] +=1
            else :
                hash_table[t] =1
    print('słowa:' ,words, " litery:", letters)
    print("Częstotliwosc:", hash_table)

#%%

# Counting words, letters and frequency of letters in string  my second approach:
def counting_function2(text) :
    words = 1
    letters =0
    hash_table = {}
    for t in text :
        if t == ' ' :
            words += 1
        else :
            t = t.lower()
            letters +=1
            if t in hash_table :
                hash_table[t] +=1
            else :
                hash_table[t] =1
    print('W naszym tekscie: "', text, '"  znajdujemy: ',words, 'słów oraz ', letters, 'znaków (bez spacji).')
    print("Częstotliwosc liter jest następująca:", hash_table)


