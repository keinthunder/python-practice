#    question 1 print all positive and negative numbers seperately
l=[1,-3,4,-67,34]
positive=[]
negative=[]
for i in l:
    if i<0:
        negative.append(i)
    elif i>=0:
        positive.append(i)
print(f'positve={positive}\nnegative={negative}'

#    question 2 find the mean/average of all elements of the list
l=[12,45,768,97]
total=0
for i in l:
    total+=i
avg=total/len(l)
print(avg)

#    question 3 find the greatest element and find it's index
l=[12,35,26,678,0,5]
indexx=0
for i in l:
    a=0
    for j in l:
        if i>=j:
            a+=1
    if a==len(l):
        print(f'greatest value is {i}\n index={indexx}')
        break
    indexx+=1
#     or
largest=l[0]
index=0
for i in range(len(l)):
    if l[i]>largest:
        largest=l[i]
        index=i
print(largest , index)

#    question 4 find the second greatest element
l=[5,5,2,3]
l.sort()
great=l[0]
second=l[0]
for i in l:
    if i>great:
         second=great
         great=i
    elif i>second:
         second=i
print(f'greatest value ={great}\nsecond greatest value={second}')

#    question 5 check if a list is already sorted
l=[1,2,5,86,789,4675,2345692714,564175607560]
a=1
for i in range(len(l)-1):
    if l[i]<=l[i+1]:
        a+=1
if a==len(l):
    print('it is sorted')
else:
    print('it is not sorted')

#    or

for i in range(len(l)-1):
    if l[i]>l[i+1]:
        print('it is not sorted')
        break
else:
    print('it is sorted')
