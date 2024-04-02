#Code 1
def string_reverse():  # function name is string_reverse
    store_letters=[]   # local variable list inside a function
    string_input=input("ENTER STRING: ") #taking string input
    for  letter in string_input: # iterating each letter in a string
        store_letters.append(letter) # storing each letter in a list
    store_letters.reverse() #reverse a list
    reverse_result=''.join(store_letters) #join reverse list back into string
    return reverse_result #give  result to function
print(string_reverse()) # print result by calling a function
