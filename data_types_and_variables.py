# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?
little_mermaid = 3
brother_bear = 5
hercules = 1
price_per_day = 3

total_price = (price_per_day * little_mermaid) + (price_per_day * brother_bear) + (price_per_day * hercules)
print(total_price, 'dollars')


#Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
google = 400
amazon = 380
fb = 350
fb_hours = 10
amazon_hours = 4
google_hours = 6

total_compensation = (google * google_hours) + (amazon * amazon_hours) + (fb * fb_hours)
print(total_compensation, 'dollars')


# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.
 class_not_full = True
 sched_conflicts = False
 can_enroll = class_not_full and not sched_conflicts
 print(can_enroll)


#  A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.
more_than_two_items = True
offer_expired = False
premium_member = True
can_be_applied = (more_than_two_items and not offer_expired) or  (premium_member and not offer_expired)
print(can_be_applied)

# Continue working in your data_types_and_variables.py file. Use the following code to follow the instructions below
username = 'codeup'
password = 'notastrongpassword'
pass_char_min = True
user_char_max = True
pass_not_user = True


