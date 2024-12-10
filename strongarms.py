number = int(input("Enter a number: "))
digits = len(str(number))
usersnumber = 0
temp = number

while temp > 0:
    digit = temp % 10
    usersnumber += digit ** digits
    temp //= 10

if number == usersnumber:
    print("Number is an armstrong number!")
else:
    print("Number is not an armstrong number!")