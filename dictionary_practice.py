#    question 1 merge two dictionaries into one
d1={'a':10,'b':20,'c':30}
d2={'d':40,'e':50,'f':60}
for i in d2:
    d1[i]=d2[i]
print(d1)

#    question 2 sum of all values of a dictionary
d={1:10,2:20,3:30,4:40,5:50}
sum=0
for i in d:
    sum+=d[i]
print(sum)

#    question 3 count the frequency of each element in a list uing dictionary
l=['a','b','c','a','c','c']
dict={}
for i in l:
    if i in dict.keys():
        dict[i]+=1
    else:
        dict[i]=1
print(dict)

#    #question 4 combine two dictionary and add values for common keys
d1={'a':10,'b':20,'c':30}
d2={'c':40,'d':50,'e':60}
for i in d2:
    if i in d1.keys():
        d1[i]+=d2[i]
    else:
        d1[i]=d2[i]
print(d1)

    # question 5 Count the frequency of each word in a sentence
Input="python is fun python is easy"
d={}
l=Input.split( )
for i in l:
    if i.lower() in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)

#    question 6 Find the key having the second highest value
d={"a": 20, "b": 50, "c": 40}
g1=min(d.values())
g2=min(d.values())
for i in d: 
    if d[i]>g1:
        g2=g1
        g1=d[i]
    elif d[i]>g2 and d[i]!=g1:
        g2=d[i]
print(f'second greatest value is {g2}')

#    question 7 Remove all key-value pairs whose value is less than 20
d={"a": 10, "b": 25, "c": 15, "d": 40}
dict={}
for i in d:
    if d[i]>=20:
        dict[i]=d[i]
print(dict)

#    question 8 Create a dictionary from two lists
keys = ['a', 'b', 'c']
values = [10, 20, 30]
d={}
for i in range(len(keys)):
    d[keys[i]]=values[i]
print(d)

#    question 9 Group words by their first letter
l=["apple", "ant", "ball", "bat", "cat"]
d={}
for i in l:
    if i[0] in d.keys():
        d[i[0]].append(i)
    else:
        d[i[0]]=[i]
print(d)
