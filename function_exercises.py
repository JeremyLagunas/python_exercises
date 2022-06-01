## Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(n):
    if n in [2, 'two']:
        print(True)
    else:
        print(False)
    return
is_two('two')

## 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(i):
    if i.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(True)
    else:
        print(False)
    return

is_vowel('F')

## 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(x):
    if x.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(False)
    else:
        print(True)

is_consonant('X')

## 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def capitalize_function(word):
    if word[0] in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']:
        print(word.capitalize())
    else:
        print(word)
    return

capitalize_function('apple')

## 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
tip_percentage = .20
bill_total = 79.99
def calculate_tip(bill_total):
    tip_amount = tip_percentage * bill_total
    return tip_amount

calculate_tip(bill_total)

## 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
discount_rate = .20
original_price = 89.99

def apply_discount(original_price):
    discounted_price = original_price - (original_price * discount_rate)
    return discounted_price

apply_discount(original_price)

## 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.


## 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(x):
    if x in range(90, 101):
        print('A')
    elif x in range(80, 90):
        print('B')
    elif x in range(70, 80):
        print('C')
    else:
        print('F')
    return

get_letter_grade(90)

## 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
vowels = ['a', 'e', 'i', 'o', 'u']
def remove_vowels(word):
    result = [i for i in word if i.lower() not in vowels]
    result = ''.join(result)
    print(result)
    return

remove_vowels('aeiouy')

## 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is: anything that is not a valid python identifier should be removed, leading and trailing whitespace should be removed,everything should be lowercase,spaces should be replaced with underscores



## 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.

