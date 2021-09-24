'''5. Given a list, iterate it, and display numbers divisible by five,
and if you find a number greater than 150, stopthe loop iteration.'''

list_number=[10,15,20,33,40,54,70,80,88,130,136,140,160]
for i in list_number:
    if i<150:
        if i%5==0:
            print("Number is divided by 5 = ", i)
        else:
            print("This is greater then 150")
            break

# 6. Reverse the following list using for loop

for i in reversed(list_number):
    print(i)
