## Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(n):
    if n in [2, '2']:
        print(True)
    else:
        print(False)
    return
is_two('2')

## 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(i):
    return len(i) == 1 and i.lower() in 'aeiou'

is_vowel('U')

## 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(x):
    return len(x) == 1 and x.isalpha() and not is_vowel(x)
    

is_consonant('X')

## 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def capitalize_starting_consonant(word):
    if type(word) != str:
        return False
    first_letter = word[0]
    if is_consonant(first_letter):
        word = word.capitalize()
    return word

capitalize_function('banana')

## 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tip_percentage, bill):
    tip_amount = tip_percentage * bill
    return tip_amount

calculate_tip(.2, 50)

## 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
discount_rate = .20
original_price = 89.99

def apply_discount(discount_percentage, original_price):
    discounted_price = original_price - (original_price * discount_percentage)
    return discounted_price

apply_discount(.75, 50)

## 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.


## 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(grade):
    if type(grade) == int or type(grade) == float:
            if grade >= 90:
                return 'A'
            elif grade >= 80:
                return 'B'
            elif grade >= 70:
                return 'C'
            elif grade >= 60:
                return 'D'
            else:
                return 'F'
    else:
        return 'Input must be a number'
get_letter_grade('A')

## 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(string):
    vowels = 'aeiou'
    result = [i for i in string if i.lower() not in vowels]
    result = ''.join(result)
    return result

remove_vowels('yayeYIyoyu')

## 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is: anything that is not a valid python identifier should be removed, leading and trailing whitespace should be removed,everything should be lowercase,spaces should be replaced with underscores
def remove_special_char(string):
    return ''.join([c for c in string if c.isalnum() or c == ' '])

remove_special_char('he!!0 w0rld!')

def normalize_name(string):
    special_char_removed = remove_special_char(string)
    return special_char_removed.lower().strip().replace(' ', '_')

normalize_name('apple pie is delicious')

## 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.

def cumulative_sum(nums):
    output = []
    total = 0
    for num  in nums:
        total += num
        output.append(total)
    return output

cumulative_sum([1, 2, 3, 4, 5])