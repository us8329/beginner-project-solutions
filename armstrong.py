number = int(input())
m = int(number)
counting_digits = 0
while m>0:
    d = m%10
    counting_digits += 1
    m= int(m/10)
temp = int(number)
sum = 0
while temp>0:
    d = temp%10
    x= pow(d,counting_digits)
    sum += x
    temp=int(temp/10)
if sum == number:
    print("Armstrong")
else:
    print("Not armstrong")
