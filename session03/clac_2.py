#Exercise 2

# 1. Use variable properly
# 2. format output properly by using f-string

#Question 1 
radius = 5
pi = 3.1415926
volume = (4/3 * pi *radius ** 3)
print(f"The volume of a sphere with radius 5 is {volume}.")

#Question 2
book_price = 24.95
discount = 0.4
actual_rate = (1-discount)
first_shipping_cost = 3
extra_shipping_cost = 0.75
copies = 60
copies_after_firstshipping = 60-1

total_book_price = book_price * actual_rate * copies

total_shipping_cost = (first_shipping_cost + extra_shipping_cost * copies_after_firstshipping)

total_cost = total_book_price + total_shipping_cost

print(f'The total cost is ${total_cost:0.2f}.')

#Question 3
start_time = (6*60 + 52) * 60 #start time 6:54 turning into seconds due to turning speed into seconds
easy_time = (8*60 + 15) * 2 # 8:15 per mile in seconds (starting 1 miles & ending 1 mile)
tempo_time = (7*60 + 12) *3 # 7:12 per mile in seconds (3 miles)

breakfast_time_seconds = (start_time + easy_time + tempo_time)
breakfast_time_hour = (breakfast_time_seconds / 3600) #60 minutes *60 seconds

clock_breakfast_hour = int(breakfast_time_hour)

breakfast_time_minute = (breakfast_time_hour - clock_breakfast_hour) * 60

clock_breakfast_minute = int(breakfast_time_minute)

breankfast_time = clock_breakfast_hour, clock_breakfast_minute
print(f'The breakfast time is {breankfast_time}.')

#Question 4
ori_grade = 82
new_grade = 89
difference = new_grade - ori_grade
percentage = difference / ori_grade
print (f"the percentage of increase is {percentage:3.1%}.")


