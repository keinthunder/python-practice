#   question 1 greter number between two
a=int(input('enter a number'))
b=int(input('enter another number'))
if a>b:
     print(f'{a} is greater')
else:
         print(b,' is greater')

#    question 2 enter gender and get a greeting message
input= input('enter your gender').lower()
if input == 'male':
    print('have a nice day sir')
elif input== 'female':
    print("have a nice day ma'am")
else:
    print('have a nice day')

#    question 3 accept an integer and check whether it's even or odd
num=int(input('enter a number you want to check'))
if num%2==0:
    print(f'{num} is an even number')
else:
    print(num,'is an odd number')

#    question 4 age verification for voting
a=int(input('enter your age'))
if a>=18:
    print('you can vote')
else:
    print('you cannot vote')

#   question 5 leap year check
a=int(input('enter the year you want to check'))
if a%100!=0:
    if a%4==0:
        print('it is a leap year')
    else:
        print('it is not a leap year')
else:
    if a%400==0:
        print('it is a leap year')
    else:
        print('it is not a leap year')

#    question 6 check the temperature
temp=int(input('enter the temperature in degree celsius you want to check'))
if temp<=10:
    print('frezzing cold')
elif 10<temp<40:
    print('plesant temprature')
else:
    print('extremely hot')
