boolean = True
while boolean:
    print(boolean)
    boolean = False
    
'''----------------------------------------------------------------'''

x=10
while x>=1:
    print(x)
    x-=1
    
'''----------------------------------------------------------------'''

for x in range(1,5,1):
    print(x)
    
'''----------------------------------------------------------------'''

l=['one','two','three','four']
l.append('five')
for i in l:
    print(i, ' - ',len(i))
    
'''----------------------------------------------------------------'''

test=[1,2,3,4,5,6,7,8,9]
for i in test[1:10:2]:
    print(i)
    
'''----------------------------------------------------------------'''

l=[i for i in range(10)]
print(l)
print(any(i<5 for i in l))

'''----------------------------------------------------------------'''

# These examples below are from a Python programming YouTube video.
# Note: these examples are not my own; thus I won't take someone else's
# credit. I used these examples to gain a broader understanding of what
# Python's 'itertools' commands do...

# See Corey Schafer on YouTube for more details:

person_group=itertools.groupby(people,get_state)
for key, group in person_group:
    print(key,group)
    
'''----------------------------------------------------------------'''

letters=['a','b','c','d']
numbers=[1,2,3,2,1,0]
names=['Corey','Nicole']
result=itertools.accumulate(numbers,operator.mul)
for item in result:
    print(item)
    
'''----------------------------------------------------------------'''

letters=['a','b','c','d']
numbers=[0,1,2,3,2,1,0]
names=['Corey','Nicole']
result=itertools.accumulate(numbers,operator.mul)
for item in result:
    print(item)
    
'''----------------------------------------------------------------'''

letters=['a','b','c','d']
numbers=[0,1,2,3,2,1,0]
names=['Corey','Nicole']
result=itertools.accumulate(numbers)
for item in result:
    print(item)    
    
'''----------------------------------------------------------------'''

def lt_2(n):
    if n<2:
        return True
    return False

'''----------------------------------------------------------------'''

letters=['a','b','c','d']
numbers=[0,1,2,3,2,1,0]
names=['Corey','Nicole']
selectors=[True,True,False,True]
result=itertools.takewhile(lt_2,numbers)
for item in result:
    print(item)
    
'''----------------------------------------------------------------'''

letters=['a','b','c','d']
numbers=[0,1,2,3,2,1,0]
names=['Corey','Nicole']
selectors=[True,True,False,True]
result=itertools.dropwhile(lt_2,numbers)
for item in result:
    print(item)
    
'''----------------------------------------------------------------'''

letters=['a','b','c','d']
numbers=[0,1,2,3]
names=['Corey','Nicole']
selectors=[True,True,False,True]
result=itertools.filterfalse(lt_2,numbers)
for item in result:
    print(item)
    
'''----------------------------------------------------------------'''

letters=['a','b','c','d']
numbers=[0,1,2,3]
names=['Corey','Nicole']
selectors=[True,True,False,True]
result=filter(lt_2,numbers)
for item in result:
    print(item)
    
'''----------------------------------------------------------------'''

letters=['a','b','c','d']
numbers=[0,1,2,3]
names=['Corey','Nicole']
selectors=[True,True,False,True]
result=itertools.compress(letters,selectors)
for item in result:
    print(item)
    
'''----------------------------------------------------------------'''

with open('test.log','r') as f:
    header=itertools.islice(f,3)
    for line in header:
        print(line,end='')
        
'''----------------------------------------------------------------'''

letters=['a','b','c','d']
numbers=[0,1,2,3]
names=['Corey','Nicole']
result= itertools.islice(range(10),1,5,2)
for item in result:
    print(item)
    
'''----------------------------------------------------------------'''

letters=['a','b','c','d']
numbers=[0,1,2,3]
names=['Corey','Nicole']
result= itertools.islice(range(10),1,5)
for item in result:
    print(item)
    
'''----------------------------------------------------------------'''

letters=['a','b','c','d']
numbers=[0,1,2,3]
names=['Corey','Nicole']
result= itertools.islice(range(10),5)
for item in result:
    print(item)
    
'''----------------------------------------------------------------'''

letters=['a','b','c','d']
numbers=[0,1,2,3]
names=['Corey','Nicole']
combined=itertools.chain(letters,numbers,names)
for item in combined:
    print(item)
    
'''----------------------------------------------------------------'''

letters=['a','b','c','d']
numbers=[0,1,2,3]
names=['Corey','Nicole']
result=itertools.combinations_with_replacement(numbers,4)
for item in result:
    print(item)
    
'''----------------------------------------------------------------'''

letters=['a','b','c','d']
numbers=[0,1,2,3]
names=['Corey','Nicole']
result=itertools.product(numbers,repeat=4)
for item in result:
    print(item)
    
'''----------------------------------------------------------------'''

letters=['a','b','c','d']
numbers=[0,1,2,3]
names=['Corey','Nicole']
result=itertools.permutations(letters,2)
for item in result:
    print(item)
    
'''----------------------------------------------------------------'''

letters=['a','b','c','d']
numbers=[0,1,2,3]
names=['Corey','Nicole']
result=itertools.combinations(letters,2)
for item in result:
    print(item)
    
'''----------------------------------------------------------------'''
    
# A stern thanks to Corey Schafer, these examples below are my own
# spin on what I've learned from watching his Python programming
# YouTube videos.

squares=itertools.starmap(pow,[(0,2),(1,2),(2,2)])
print(list(squares))

'''----------------------------------------------------------------'''

squares=map(pow,range(10),itertools.repeat(2))
print(list(squares))
counter=itertools.repeat(2,times=3)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

'''----------------------------------------------------------------'''

counter=itertools.repeat(2)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

'''----------------------------------------------------------------'''

counter=itertools.cycle(('On','Off'))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

'''----------------------------------------------------------------'''

counter=itertools.cycle([1,2,3])
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

'''----------------------------------------------------------------'''

counter= itertools.count()
data=[100,200,300,400]
daily_data=list(itertools.zip_longest(range(10),data))
print(daily_data)

'''----------------------------------------------------------------'''

counter=itertools.count(start=5,step=-2.5 )
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

'''----------------------------------------------------------------'''

counter= itertools.count()
for num in counter:
    print(num)
    
'''----------------------------------------------------------------'''

counter= itertools.count()
data=[100,200,300,400]
daily_data=list(zip(itertools.count(),data))
print(daily_data)

'''----------------------------------------------------------------'''

nums=[1,2,3]
i_nums=iter(nums)
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
