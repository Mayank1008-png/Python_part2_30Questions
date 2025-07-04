#SETS 10 QUESTIONS
#ans1
set1={1,2,3}
set2={4,5,6}
print(set2.union(set1))
#ans2
set3={1,2,3,4}
set4={6,5,4,3}
print(set4.intersection(set3))
#ans3
set5={1,2,3,4,5,6}
set6={5,6}
print(set6.issubset(set5))
#ans4
set7={1,2,3,4,5,6,7,8,9}
set8={4,5,10}
print(set7.difference(set8))
#ans5
set9={1,2,3,4,5,6}
set10={6,7,8}
print(set9.symmetric_difference(set10))
#ans6
set11={1,2,3,4,5}
set11.discard(5)
print(set11)
#ans7
text=input('Enter any string=')
word=text.split()
print(word)
set12=set(word)
print('UNIQUE WORDS=')
for i in set12:
    print(i)
#ans8
list1=[1,2,3,4,5,4,3,2,1]
set13=set(list1)
print(set13)
#ans9
set14={1,2,3,4,5}
set15={6,7,8,5}
set16=set14.intersection(set15)
print(set16)
if set16==set():
    print("No element is common")
else:
    print("Common elements are:=",set16)
#ans10
set17={x**2 for x in range(1,11)}
print("square of 1 to 10 is =",set17)

#DICTIONARY 10 QUESTIONS
#ans 1
text1=input('enter a string=')
char_freq={}
for i in text1:
    if i in char_freq:
        char_freq[i]+=1
    else:
        char_freq[i]=1
print('character frequencies:')
for i,a in char_freq.items():
    print(f'{i}:{a}')
#ans2
emp_salary={
    'mohan':20000,
    'sohan':30000,
    'rohan':45000
}
max_salary=max(emp_salary,key=emp_salary.get)
print("max salary is=",max_salary)
#ans3
score={
    'physics':98,
    'maths':99,
    'chemistry':97
}
swap={value:key for key,value in score.items()}
print(swap)
#ans4
dict1={
    'name1':'mayank',
    'name2':'Rohan'
}
dict2={
    'name3':'kittu',
    'name4':'bittu'
}
dict1.update(dict2)
print(dict1)
#ans5
info={
    'name':'mayank',
    'age':20,
    'mobile':9090999990
}
find='age'
if find in info:
    print(f'{find} exist with a value {info["age"]}')
else:
    print(f'{find} does not exist')
#ans6
score1={
    'physics':98,
    'maths':99,
    'chemistry':97
}
mark=dict(sorted(score1.items(),key=lambda item: item[1]))
print(score1)
#ans7
info1={
    'name':'mayank',
    'age':20,
    'mobile':9090999990
}
info1.pop('mobile')
print(info1)
#ans8
score1={
    'physics':98,
    'maths':99,
    'chemistry':97
}
total_marks=0
for i in  score1.values():
    total_marks+=i
print(total_marks)
#ans9
lst1=['a1','a2','a3']
lst2=[10,12,13]
dict3={}
for x,y in zip(lst1,lst2):
    dict3.update({x:y})
print(dict3)
#ans10
my_dict={'a':10,'b':12,'c':13,'d':10}
list11=list(my_dict.values())
count1={value for value in list11 if list11.count(value)>1}
print(count1)


#TUPLE
#ans1
tup1=(1,2,3,4,5,6)
total=0
for i in tup1:
    total+=i
print(total)
#ans2
lst3=[1,2,3,4,5,6,2]
tup2=tuple(lst3)
print(tup2)
#ans3
tup3=('m','a','y','a','n','k')

str2=''.join(tup3)
print(str2)
#ans4
tup4=(9,8,7,0,3)
for i in range(len(tup4)):
    print(f'{i}={tup4[i]}')
#ans5
tup5=(1,4,2,3,5,6,2,2,2)
tupe=2
print(tup5.count(tupe))
#ans6
tup6=('a','b','c','d','a')
i=0
for i in tup6:
    print(i)
#ans7
tup6=('a','b','c','d','a')
print(tup6[::-1])
#ans8
t=(1,(2,3),4)
print(t[1][0])
#ans9
tup7=(1,2,3,4,5)
num=5
for i in (tup7):
    if i == num:
        print(f'yes {num} is present at index {i}')
    else:
        print(f'sorry {num} not at index {i}')
#ans10
tup8=(1,2,3,4)
lst4=list(tup8)
lst4.remove(3)
tup9=tuple(lst4)
print(tup9)
