#Question 1
print ("Q1.1: 5, integer")
print ("Q1.2: Float") 
print ("Q1.3: Name Error")
print ("Q1.4: 3, integer")
print ("Q1.5: true, boolean")
print ("Q1.6: true, boolean")
print ()

#Question 2
print("Q2.1: false")
print("Q2.2: false")
print("Q2.3: true")
print("Q2.4: false")
print()

#Question 3
import time

seconds= time.time()
seconds_day = 24*60*60
seconds_hour = 60*60
seconds_minute = 60

clock_days = seconds//seconds_day
ad = seconds/seconds_day
clock_hours=int((ad-clock_days)*24)
ah=(ad-clock_days)*24

clock_minutes = int(ah-clock_hours)*60
am=(ah-clock_hours)*60
clock_seconds = int((am-clock_minutes)*60)

print(f"Q3: Days: {clock_days} Hours: {clock_hours} Minutes: {clock_minutes} Seconds: {clock_seconds}")


