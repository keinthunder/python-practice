#    question 1 print all positive and negative numbers seperately
l=[1,-3,4,-67,34]
positive=[]
negative=[]
for i in l:
    if i<0:
        negative.append(i)
    elif i>=0:
        positive.append(i)
print(f'positve={positive}\nnegative={negative}')

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

    # question 6 move all zeros to the end
l=[1, 0, 2, 0, 3, 4, 0]
for i in range(len(l)):
    if l[i]==0:
        a=l.pop(i)
        l.append(a)
print(l)

#    question 7 find all duplicates elements
l=[1, 2, 3, 2, 4, 5, 1, 6]
check=[]
dup=[]
for i in l:
    if i in check:
        dup.append(i)
    else:
        check.append(i)
print(dup)

#    question 8 find the third largest element
l=[10, 45, 23, 89, 67, 89 , 67]
g1=l[0]
g2=l[0]
g3=l[0]
for i in l:
    if i>g1:
        g3=g2
        g2=g1
        g1=i
    elif i>g2 and i!=g1:
        g3=g2
        g2=i
    elif i>g3 and i!=g1 and i!=g2:
        g3=i
print(g3)

#    question 9 Find the pair of numbers whose sum is equal to a given target
list = [2, 7, 11, 15]
l=[]
target=9
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]+list[j]==target:
            l.append(list[i])
            l.append(list[j])
print(l)
        
#    question 10 Rotate the list to the right by k positions
list = [1, 2, 3, 4, 5]
k = 2
list=list[-k:]+list[:-k]
print(list)
#    or
list = [1, 2, 3, 4, 5]
k = 2
for i in range(k):
    last=list[-1]
    for j in range(len(list)-1,0,-1):
        list[j]=list[j-1]
    list[0]=last
print(list)
