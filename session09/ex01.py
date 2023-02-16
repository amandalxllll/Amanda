import cmath #It succesfully runned for the first time but does not work for the second time; even if I format it
# Exercise 1
r = 0
for i in range(1, 11):
    r += i
print(r)

b = 0

for i in range(1, 1000):
    b += i
print(b)

n = 0
for i in range(1, 1000):
    if i % 2 == 1:
        n += 1
print(n)
