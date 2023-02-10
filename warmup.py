'''                                         Question_01: 
Ask for the user’s first name and then ask for their surname and display the output message as Hello [First Name] [Surname].'''


firstname = input("Enter your first name: ")
surname = input("Enter your sur-name: ")
print("Hello" , firstname , surname)



'''                                        Question-02 
Ask the user to enter two numbers and display total as answer.'''


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
add = num1 + num2
print("Sum of two number is: " , add)


'''                                        Question-03
Ask for the total price of the bill, then ask how many diners there are and then display the dinner share of each person must pay.'''


totalbill = int(input("Enter total bill :"))
numofpeople = int(input("Enter number of people: "))
eachpay = totalbill/numofpeople
print("Each person will pay: " , eachpay)



'''                                        Question-04
Write a program that will ask for a number of days and then will show how many hours, minutes and seconds are in that number of days.'''


days = int(input("Enter a number of days: "))
hours = days*24
minutes = hours*60
seconds = minutes*60
print("Number of days is: " , days)
print("Number of hours is: " , hours)
print("Number of minutes is: " , minutes)
print("Number of seconds is: " , seconds)



'''                                        Question-05
Ask the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller number goes into the larger number in a user-friendly format'''


num1 = int(input("Enter a number over 100: "))
num2 = int(input("Enter a number under 10: "))
asd = num1/num2
print("The smaller number goes into the larger number by: " , asd)