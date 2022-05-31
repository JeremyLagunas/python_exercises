## 1. a.  
day_of_the_week = input("Enter the day of the week: ")
print(day_of_the_week)
if day_of_the_week.lower == 'monday':
    print('yes, today is monday')
else:
    print('no, today is not monday')

## 1. b.
day_of_the_week = input("Enter the day of the week: ")
print(day_of_the_week)
if day_of_the_week.lower == 'saturday':
    print('weekend')
elif day_of_the_week.lower == 'sunday':
    print('weekend')
elif day_of_the_week.lower == 'monday':
    print('week day')
elif day_of_the_week.lower == 'tuesday':
    print('week day')
elif day_of_the_week.lower == 'wednesday':
    print('week day')
elif day_of_the_week.lower == 'thursday':
    print('week day')
else:
    print('week day')

## 1. c.
weekly_hours_worked = 40
hourly_rate = 20
week_paycheck = weekly_hours_worked * hourly_rate
print(week_paycheck, 'dollars')


## 2. a. 
i = 5
while i <= 15:
    print(i)
    i += 1

e = 0
while e <= 98:
    print(e)
    e += 2

e

while e >= -10:
    print(e)
    e-= 5

u = 2
while u < 1000000:
    print(u)
    u **= 2

w = 100
while w >= 5:
    print (w)
    w -= 5

## 2. b. i.  Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
user_input = int(input('please input a number: '))
no_list = [1,2,3,4,5,6,7,8,9,10]
for i in no_list:
    print(f'{i} * {user_input} = {i * user_input}')

## 2. b. ii. Create a for loop that uses print to create the output shown below.
no_list2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in no_list2:
    if i == '1':
        print(i * 1)
    elif i == '2':
        print(i * 2)
    elif i == '3':
        print(i * 3)
    elif i == '4':
        print(i * 4)
    elif i == '5':
        print(i * 5)
    elif i == '6':
        print(i * 6)
    elif i == '7':
        print (i * 7)
    elif i == '8':
        print (i * 8)
    elif i == '9':
        print(i * 9)

## 2. c. 
odd_no = int(input('please enter an odd number between 1 and 50: '))
while (odd_no % 2) == 0:
    print('incorrect value, please enter an odd number between 1 and 50')
    odd_no = int(input('please enter an odd number between 1 and 50: '))

odd_no
range(50)
for i in range(50):
    if (i % 2) == 0:
        continue
    print(f'Here is an odd number: {i}')
    if i == odd_no:
        print(f'Yikes! Skipping number: {i}')

## 2. d.
pos_no = int(input('please enter a positive number: '))
pos_no
while pos_no < 1:
    print('incorrect value')
    pos_no = int(input('please enter a positive number: '))

while pos_no > 0:
    


## 2. e.
while pos_no > 1:
    print(pos_no)
    pos_no -= 1
    