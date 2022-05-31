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
    if i in ['a', 'e', 'i', 'o', 'u']:
        print(True)
    else:
        print(False)
    return

is_vowel('i')

## 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(x):
    if x.lower