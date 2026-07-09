#    question 1 print hello world n times
n=int(input('enter how many time u want to print hello world'))
for i in range(n):
    print('hello world')

#    question 2 print natural number from 1 to n
n=int( input('enter how many natural numbers you want'))
for i in range(1,n+1):
    print(i)

#    question 3 print n down to 1
n=int( input('enter your number'))
for i in range(n,0,-1):
    print(i)

#    question 4 multiplication table of n number
n=int( input('enter your number'))
for i in range(1,11):
    print(n,'x',i,'=',n*i)

#    question 5 sum of first n natural numbers
n=int( input('enter your number'))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)

#    question 6 factorial of first n natural numbers
n=int( input('enter your number'))
fac=1
for i in range(1,n+1):
    fac=fac*i
print(fac)

#    question 7 sum of all even and odd number seperately
n=int( input('enter your number'))
even=0
odd=0
for i in range(1,n+1):
    if i%2==0:
        even+=i
    else:
        odd+=i
print(f'summ of even numbers = {even}')
print(f'summ of odd numbers = {odd}')

#    question 8 print all factors of a number
n=int( input('enter your number'))
for i in range(1,n+1):
    if n%i==0:
        print(i,end=',')

#    question 9 check if the number is perfect{sum of factors(excluding the self number) = number itself}
n=int( input('enter your number'))
sf=0
for i in range(1,n):
    if n%i==0:
        sf+=i
if sf==n:
    print("it's a perfect number")
else:
    print("it's not a perfect number")

#    question 10 check if a number is prime
n=int( input('enter your number'))
a=0
for i in range(1,n+1):
    if n%i==0:
        a+=1        
if a==2:
    print('it is a prime number')
else:   
    print('it is not a prime number')

#    question 11 reverse the string without using built in function
n=input('enter your word')
rev=''
for i in range(-1,-len(n)-1,-1):
    rev+=n[i]
print(rev)    

#    question 12 check if a string is palindrome or not
n=input('enter your word')
str=''
for i in range(len(n)-1,-1,-1):
    str+=n[i]
if str==n:
    print('it is a palindrome')
else:
    print('it is not a palindrome')

#    question 13 count letters, numnbers and special character in a string
n=input('enter your word').lower()
num=0
alpha=0
special=0
for i in n:
    if i in 'abcdefghijklmnopqrstuvwxyz':
        alpha+=1
    elif i in '0123456789':
        num+=1
    else:
        special+=1
print(f'letters are{alpha} numbers are{num} special characters are{special}')

#  same answer but with using unicode or ascivalue
n=input('enter your word').lower()
num=0
alpha=0
special=0
for i in n:
    if 65<=ord(i)<=90 or 97<=ord(i)<=122 :
        alpha+=1
    elif 48<=ord(i)<=57:
        num+=1
    else:
        special+=1
print(f'letters are{alpha} numbers are{num} special characters are{special}')

#    question 14 seperate each didgit of a number and print it on a different line
n=int(input('enter a number'))
rev=0
while n!=0:
    print(n%10)
    rev=(rev*10)+(n%10)  
    n//=10
print(rev)

    # question 15 check if a number is aplindrome or not
a=n=int(input('enter a number'))
rev=0
while n>0:
    rev=rev*10+n%10    # imp algebraic expression to get reverse number
    n//=10
if rev==a:
    print('it is a palindrome')
else:
    print('it is not a palindrome')
