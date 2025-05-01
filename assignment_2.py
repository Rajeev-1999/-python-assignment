# check number is even or odd

number = int(input("Enter Number here : "))

if number == 0:
    print("This is not even or nor odd ",number)
elif number % 2 == 0:
    print("This is Even Number : ",number)
else:
    print("This is Odd number : ",number)





sum = 0

for num in range(1,51):
    sum += num
  #  print("Num is : ",num)
    print("Sum is : ",sum)



