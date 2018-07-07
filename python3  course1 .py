

pycharm is commercail 
    => community edition of pycharm is free
    https://www.jetbrains.com/pycharm
configure=>settings=> (serach  project interpreter ) ->
	
https://www.python.org/downloads/     => download Windows x86-64 executable installer
	https://www.youtube.com/watch?v=0y5XlNeFxNk
====================================================
Instructor
Rob Gance email:  gancelot@yahoo.com
Student Manual:    
https://www.dropbox.com/s/d0ijr59fbodkxb5/IN1467%20Intensive%20Introduction%20to%20Python.pdf?dl=0
Instructor Slides:   
https://www.dropbox.com/s/yehczglqt4mmjcm/IN1467_Intensive_Introduction_to_Python_instructor_slides.pdf?dl=0
Student files:   
https://www.dropbox.com/s/nko3ugjkwcukmq0/IN1467_student_files.zip?dl=0
===========================================================   
pycharm 
  file -> settings -> Project: student_files -> Project  Interpreter (here you can select the python interpretor)
  tools ->  Python console 

============================================= 
https://regex101.com/tests
https://txt2re.com/
gancelot@yahoo.com  

Good url:
https://automatetheboringstuff.com

Similar to our course, nothing advanced:
https://python.swaroopch.com/stdlib.html

Another Python tutorial:     
http://thepythonguru.com/    

Long, time, recommended Python tutorial resource:    
https://learnpythonthehardway.org/book/    

Decebt slide-based tutorial:    
https://stephensugden.com/crash_into_python/     

Contains some intermediate topics (generators, decorators, ...):     
http://www.learnpython.org/      

http://www.diveintopython3.net/    

***********************************************************************************************



---------------------------------------------------------------------------------------------
import sys
print(sys.version)

C:\ProgramData\Anaconda3\python.exe
C:\Users\dtc_train_wsnc_wec8\Documents\student_files\ch01_overview\04_sorting.py

def my_func(greeting):
    print(greeting)

my_func('hello')
--------------------------
•Strings are immutable sequencesof Unicode characters
–Type: str
–Formal notation:my_str= str('Python is great!')
–Literal notation:my_str= 'Python is great!'


 –May use single or double quotes  (PEP-8 does not have a preference)
 -Triple quoted strings can span multiple lines. A common use is for documentation (called a docstring).
my_str= 'Python\'s great fun'
my_str= "Python is great fun"
my_str= """Python is so much fun"""

•Strings are sequences and therefore support random access:
my_str= 'Python is fun'
print(my_str[0]) # 'P'

•Sequences may be sliced (sub-sequenced):
slice = string[start : end : step]
-tartval(included)
-endval(excluded)
print(my_str[0:9]) # 'Python is'
print(my_str[:3]) # 'Pyt'
print(my_str[3:]) # 'hon is fun'
print(my_str[-1]) # 'n'
Tip:
copy = sequence[ : ]
makes a shallow copy

•Strings may be concatenated (creates a new string):
my_str= 'Python is '
new_str= my_str+'fun'
•Long strings may be continued:
my_str= 'I just cannot seem \
to finish this \
darn string!'
•Strings (sequences) may be replicated:
'hello' * 3  
  hellohellohello
•join()  ->Concatenates a list of strings using the specified separator string
	nums= ['1','2', '3']
	' '.join(nums)# 1 2 3


•split() ->Creates a list of strings based on a specifiedseparator string
	my_str= 'Python is great'
	my_list= my_str.split(' ')# Results: ['Python', 'is', 'great']

•replace()  -> Returns a new stringwith all matching substrings replaced by the new one
	my_str.replace('is', 'is still')# yields: 'Python is still great'

*strip()   ->  Returns a new string with whitespace removed from each end
	new_str= ' Whitespace will be removed. '.strip()
•find()  -> Finds the index of the first occurrence of the substring
	my_str= 'Python is great'
	my_str.find('is')# returns 7
	my_str.find('not')# returns -1
•str()  -> String class constructoraccepts any object returns a string object
	s = str(55)# creates a string from the int
	s = str(3.14)# creates a string from the float
•Use the type name as a function to perform conversions
	s1 = str(55)# '55'
	s2 = str(3.14)# '3.14'
	i1 = int('37')# 37
	i2 = int(3.14)# 3
	f1 = float(55)# 55.0
	f2 = float('3.14')# 3.14
•If a conversion cannot be made, a ValueErroris raised:
	int('hello')
	ValueError: invalid literal for int() with base 10: 'hello'

===String format()
•A preferredway to format data is to use the format() method of the string class
	s = 'It has been raining for {0}{1}and{0}{2}'
	new_str= s.format(40, 'days', 'nights')
	'It has been raining for 40 days and 40 nights'

	{ fieldname | index [!spec] [:format] }
	s6 = '{lang} is over {0:0.2f} {date} old.'.format(20, date='years', lang='Python')
		Python is over 20.00 years old.
	# format() examples:
	print('{0:>9}'.format('101.55'))  # 101.55 (field-width of 9, > right aligned, remaining space fill substitute character)
	print('{0:->9}'.format('101.55')) #  ---101.55  
	print('{0:-<9}'.format('101.55')) #  101.55---  ( < left aligned, remaining space fill substitute character)
	print('{0:-^20}'.format('hello')) # -------hello--------(^ is center aligned,field-width 20,fill - remaining space)

•Additional string class methods include:
capitalize()
center(width, char)
count(str)
endswith(str)
expandtabs()
index()
join(sequence)
ljust(width, char)
lower()
isalnum()
isalpha
isdecimal()
isdigit()
isidentifier()
islower()
isnumeric()
isprintable()
isspace()
istitle()
isupper()


Sequences
•Sequences are ordered collections of objects
	–Types include: str, list, tuple, range
	dirs= ['North', 'South', 'East', 'West']
•Common sequence capabilities:
–Random access, slicing
	dirs[2]# 'East'
	dirs[-2:]# ['East', 'West']
–Concatenation	
	dirs+ ['NW', 'NE', 'SW', 'SE']
–Replication
	dirs* 2 # ['North', 'South', 'East', 'West','North', 'South', 'East', 'West']
–Membership
	if 'east'.capitalize() in dirs:print(dirs.index('east'.capitalize()))

•Lists -mutable, ordered collections of objects
my_list= []
my_list= [1, 3, 5]
my_list= [3.3, 'hello', Person()]
my_list= list('hello')
my_list= [3.3, 'hello', Person(), 3.3, Person()]  #Lists may contain duplicates 
	
my_list= [1, 2, 3]
my_list.append(10)
my_list.insert(1, 'hello')    #1, 'hello', 2, 3, 10

===Tuples
•Tuples -immutable, ordered collections of objects
my_tuple= ()   #Empty tuple
my_tuple= (1, 3, 5)
my_tuple= (3.3, 'hello', Person())
my_tuple= tuple()   #Empty tuple
my_tuple= tuple('hello')  #tuple(sequence)
my_tuple= (1,)    #tuple with one element

my_list = [4, 5, 6]
t = (my_list, 2, 3)
t[0] = my_list2   ----> this will cuase error
print(t)

my_list = [4, 5, 6]
t = (my_list, 2, 3)
t[0].append(10)   --> is allowed , it adding to my_list in the tuple
print(t)

===Useful Sequence Functions
•len()
dirs= ['North', 'South', 'East', 'West']   
print(len(dirs), len(dirs[0]))  
  4, 5
•max()
	max([1973, 2001, 2015, 2013, 1994])  # 2015
•min()
	min([1973, 2001, 2015, 2013, 1994])  # 1973

===Illegal Operations
•The following operationsmay notbe performed on sequences:
[1, 2, 3] + 'Bob'
[1, 2, 3] + (4, 5, 6)  
      Can't concatenate different sequence types
my_list= []
my_list[0] = 'Bob'
	Empty list to begin with, so there is no 0thaddress to assign something into
my_list= [None] * 5
my_list[0] = 37
my_list[1] = 'Bob'
	This approach is legal because the list is sized to begin
 
===Control Structures
if test:
<one or more statements>
eliftest2:   #There may be zero or more elifbranches
<one or more statements>
else:    #The elseis optional
<one or more statements>

if test:
    print('This is part of the if block!')
    print('So is this!')
print('This is not!')
	Beginning and ending of blocks are determined by indentations (use 4 spaces)

===Truthy/ FalseyValues
  Test conditions in control structures expect a bool
       However, everything in Python can evaluate to a Trueor Falsevalue
These values are all considered False:
False
None
0
0.0
''
[]
()
{}
Everything else evaluates to True!
data = [1, 2, 3]
if len(data):
    print('Datanot empty.')
Comparison Operators
•Below are a few of the comparison operators that may be used in tests:
a == b
a < b
a > b
a >= b
a <= b
a != b
a is b (same object)
a is not b
a in y (a member of)
a not in y
not a
a and b(and, or both short circuit)
a or b

===Conditional Expressions (Ternary Operator)  
•Python has a version of a ternary operator:
	username = input('Enter username--> ')   #Prompts user for input returning a string after Enter key is pressed  
    is_valid= True if len(username) > 6 else False
        Sets is_validto Trueif conditional is True otherwise sets it to False  
===Iterative Control Structures  
while test:
	<one or more statements>  
else:
	<one or more statements>
       Optional else block is only executed if conditional terminates naturally (without a break)  
	elseblock not commonly used  

for one_itemin collection:
	<one or more statements>
else:
	<one or more statements>
	Optional else only executed if conditional terminates naturally

while True:
     name = input('Enter name: ')
     if not name:
         break
      process_name(name)
	This loops until just the Enterkey is pressed
	process_name()is just a user-defined function here




====Write a script that finds the domain nameof a URL
prefixes = ['http://', 'https://']
suffixes = [':', '/', '?']
urls = ['https://docs.python.org/3/',
        'https://www.google.com?gwrs_rd=ssl#q=python',
        'http://localhost:8005/contact/501'
        ]
print(urls)
for url in urls:
    for prefix in prefixes:
        if url.startswith(prefix):
            domain = url[len(prefix):]
    for suffix in suffixes:
        pos = domain.find(suffix)
        if pos != -1:
            domain = domain[:pos]
    print(domain)
====================================
Task 1-3
---program to count a word in files in given directory
import sys
import os

args = sys.argv                                                 # get command-line args
if len(args) != 3:
    print('Improper arguments provided. Syntax:')
    print('python task1_3.py wordexpression directory')
#    sys.exit(42)

wordexpression = args[1]
directory = args[2]

wordexpression = 'print'
directory = '..'
file_list = []

dir_contents = os.listdir(directory)

for entry in dir_contents:                                  # check each item if it is a file or not
    filename = os.path.join(directory, entry)
    if os.path.isfile(filename):
        file_list.append(filename)                          # add only files to the file_list


print(file_list)
for filepath in file_list:
    line_count = 0
    for line in open(filepath):
        line_count += 1
        filename = os.path.basename(filepath)
        if line.find(wordexpression) is not -1:
            print('File: {0}, Line: {1}, ({2})'.format(filename, line_count, wordexpression))
=====================================================

in pycharm  
   tools -> Python Console   =>  to get python console  in pycharm
in pycharm 
   highlight a function of module  then 
   view -> quick definition   (for help)
   view -> quick Documentaiton 
  
dir(os)     # it will give items in a  module
dir(os.path)  

help(os.path)
help(os.path.join)  # help on usage of the module


 

===More with Lists
•Useful list methods:
append(item)adds item to the end of the list
insert(pos, item)adds item at poslocation
index(item)finds the first occurrence or -1
sort()sorts in-place
extend(lst2)similar to list1 += list2
reverse()reverses the order of the list
pop()returns/removes last item
remove(item)removes first occurrence of item

===Additional Iterating Techniques
•Use enumerate() to obtain access to both the indexand the valuewhen iterating:
weekdays = [
'Monday','Tuesday',
'Wednesday','Thursday','Friday'
]  
for idx, value in enumerate(weekdays):
  print(idx, value)
0 Monday
1 Tuesday
2 Wednesday
3 Thursday
4 Friday
   # note index start at 0 if no starting point given

for idx , item in enumerate([5,8,11,13],20):
    print('index is {}; val is {}'.format(idx,item))
index is 20; val is 5
index is 21; val is 8
index is 22; val is 11
index is 23; val is 13

for ind, val in enumerate(range(-5, 5,3),-4):
    print('ind is {}; val is {}'.format(ind, val))
ind is -4; val is -5
ind is -3; val is -2
ind is -2; val is 1
ind is -1; val is 4

•Use reversed()to iterate from the end to start:
for value in reversed(weekdays):
    print(value)
Friday
Thursday
Wednesday
Tuesday
Monday

===Iterating Multiple Collections
•Another useful function to assist with processing lists in parallel is zip():
fruit= ['Apple', 'Orange', 'Banana', 'Watermelon']
color= ['red', 'orange', 'yellow', 'green', 'blue']
for f, cin zip(fruit, color):
print('The {0} is {1}'.format(f, c))
The Apple is red
The Orange is orange
The Banana is yellow
The Watermelon is green

===Sorting === pdf slide 61 ====
•Use sort()for simple, in-placesorting:
items = [37, 2, 0, -14]
items.sort()
print(items)# [-14, 0, 2, 37]
•Use sorted()to return a list
–sorted() is ideal for immutable types such as tuples
new_items= sorted(items)  
print(new_items) # [-14, 0, 2, 37]  
  #items can be any iterable
•Using reverse=Trueas an argument will sort from largest to smallest:
	items = [37, -14, 0, 2]
	items.sort(reverse=True)
new_items= sorted(items, reverse=True)print(items, new_items)
	[37, 2, 0, -14] [37, 2, 0, -14]

===Sorting Using a Key
•Specialized sorting can be accomplished using a function (key) that defines what to compare

nums = ['13', '1', '11', '4']
nums.sort()
print(nums)

def sort_func(val):
    return int(val)
nums.sort(key=sort_func)
print(nums)

def sort_func(val):
    return int(val)
nums2 = sorted(nums, key=sort_func)
print(nums2)

===•Lambdas are inline-functions
	–For quick, short, throw away uses such as sorting, closures, functional programming
		funcName= lambda <arguments> : <expression>

	–Can be used anywhere functions are used
	•type() for a lambda returns<type 'function'>

def sort_func(val):
   return int(val) 
..equivalent to...
lambda val: int(val)
---------
•Sorting a list of records by age (descending)
records = [('John', 'Smith', 43, 'jsbrony@yahoo.com'),
           ('Ellen', 'James', 32, 'jamestel@google.com'),
           ('Sally', 'Edwards', 36, 'steclone@yahoo.com'),
           ('Keith', 'Cramer', 29, 'kcramer@sintech.com')
     ]
records.sort(key=lambda one_rec: one_rec[2], reverse=True)
print(records)
[('John', 'Smith', 43, 'jsbrony@yahoo.com'),
('Sally', 'Edwards', 36, 'steclone@yahoo.com'),
('Ellen', 'James', 32, 'jamestel@google.com'),
('Keith', 'Cramer', 29, 'kcramer@sintech.com')]
--------------------------------------
===Copying Lists
•Classic approach uses slicing
a= [ 1, 'hello', ['up', 'down'] ]
b= a[:]   #Makes a shallow copy, doesn't work for all sequence types such as generators, tends to be fastest
•Constructor approach
b = list(a)  #Works with all sequence types, still a shallow copy only

•Deep copy  #Makes a deep copy, slowest in performance
import copy
b = copy.deepcopy(a)
b[2][0] = 'backward'
print(a, b)
	[1, 'hello', ['up', 'down']] [1, 'hello', ['backward', 'down']]

---------------------------------
Task 1-4  
read files from a dir and sort them on size
import glob
import os
#path = input('Path pattern to search: ')        # example: *.py
path='../*'
files = []
files2 = []
dir_items = glob.glob(path)
print(dir_items)
for item in dir_items:
    if os.path.isfile(item):
        files.append(item)
        filesize = os.stat(item).st_size
        filename = os.path.basename(item)
        files2.append((filename, filesize))
#files.sort(key=lambda a: os.stat(a).st_size, reverse=True)
#print(files)
def sort_func(item1):
	return os.stat(item1).st_size
files.sort(key=sort_func,reverse=True)
print(files)

files2.sort(key=lambda rec1:rec1[1])
for item in files2:
    print(' nmae= {}  size= {}'.format(item[0],item[1]))


=================================================================
feb 6   2018 
slide 69 
===List Comprehensions
•List comprehensions provide a Pythonic way to make lists from other lists
–Similar to loops and they take the following form:
newlist= [ expression for varin iterable]
list1 = [1, 2, 3, 4, 5]
list2 = [x*2 for x in list1]
print(list2)   #[2, 4, 6, 8, 10]

newlist= [ expression for varin iterable test_condition]
list1 = [1, 2, 3, 4, 5]
list2 = [x*2 for x in list1 if x % 2 == 0]
print(list2)  #[ 4, 8]

EX:=====Task1-5
import glob
import os
path = '../*'
dir_contents = glob.glob(path)
files = [item for item in dir_contents if os.path.isfile(item)]
files.sort(key=lambda rec1: os.stat(rec1).st_size)
print(files)
files = [(item,os.stat(item).st_size) for item in dir_contents if os.path.isfile(item)]
files.sort(key=lambda rec1: rec1[1])
print(files)

----------------------------------------------
===Named Tuples
•Named tuples are tuples that support names instead of indices
–Similar to but simpler than creating classes
–They are ordered, more readable than dictionaries


from collectionsimport namedtuple  #Import the namedtuple()function from the collections module
Contact= namedtuple('Contact', 'first last age email')
	#Can be a space-separated stringof properties or a list of strings
records = [Contact('John', 'Smith', 43, 'jsbrony@yahoo.com'),
Contact('Ellen', 'James', 32, 'jamestel@google.com'),
Contact('Sally', 'Edwards', 36, 'steclone@yahoo.com'),
Contact('Keith', 'Cramer', 29, 'kcramer@sintech.com'),
]

records.sort(key=lambda one_rec: one_rec.age, reverse=True)
for record in records:
	print(record.last, record.age)

--------
import  collections
person =  collections.namedtuple('personType','name age')
plist=person('sally',35)
print(plist[0])
print(plist.name)
----------------
===Sets
•Sets are collections that disallow duplicate items
–Unordered, iterable, mutable
–Support len(), in, comparisons
–Members must be hashable (immutable) such as int, float, str, tuple
–Disallows list, dict, set, custom objects
–frozensetis an immutable set version
s1 = set([1, 2, 3, 2])
print(len(s1)) # 3
s2 = {4, 5, 6}  
print(s1.isdisjoint(s2)) # True
s3 = frozenset([2, 4, 7])
print(s2.difference(s3)) # {5, 6}
===Set methods
s1.issubset(s2)
s1.issuperset(s2)
s1.isdisjoint(s2)
s1.copy()
s1.add(element)
s1.clear()
s1.remove(element)
s1.intersection(s2)
s1.discard(element)

===Dictionaries
Dictionaries are collections of name/value pairs
	#In other languages we may refer to these as hashes, hashmaps, maps, lookups, tables, etc.
–Unordered, mutable, iterable
–Supports len() and in comparisons
–Keys should be hashable (immutable)
–Values may be anything
	d = { key1 : value1, key2 : value2, ... }
my_dict= {}
my_dict= dict()   #empty dicts
my_dict= { 'item1' : 'value1', 'item2' : 'value2' }
my_dict= dict(item1='value1', item2='value2')

my_dict['item3'] = 'value3'  #adding / changing values
print(my_dict['item2'])     #accessing values

---Accessing Dictionaries
d1 = {'Smith': 43, 'James': 32, 'Edwards': 36, 'Cramer': 29}
•Direct accesscan generate a KeyError
d1['Smith']# returns 43
d1['Green']# generates a KeyError
•Use exception handling to deal with aKeyError
try:
value= d1['Green']# generates a KeyError
except KeyError:
value = 0
•dict.get(key) to retrieve values also:
d1.get('Edwards')# returns 36
d1.get('Green')# returns None
•dict.get(key, default) is safest
d1.get('Cramer', 0)# returns 29
d1.get('Green', 0)# returns 0

---Iterating Over Dictionaries
d1 = {'Smith': 43, 'James': 32, 'Edwards': 36, 'Cramer': 29}
•Iteratinga dictionary directly returns keys:
for item in d1:
	print(item)
Smith
Edwards
James
Cramer

•Iterating a dictionary's values:
for val in d1.values():
print(val)
43
32
29
36

•Accessing both key and value simultaneously:
for key, val in d1.items():
print('Key: {key}, Value: {val}'.format(key=key, val=val), end=' ')
	#items() returns a (view of) list of tuples

d1 = {'Smith': 43, 'James': 32, 'Edwards': 36, 'Cramer': 29}
for item in d1:
	print('key={} val={}'.format(item,d1[item]))
key=Smith val=43
key=James val=32
key=Edwards val=36
key=Cramer val=29

---Other dict methods
d1.copy()
d1.clear()
d1.fromkeys([key_seq])
d1.pop(key, def)
d1.setdefault(key, def)
d1.update(d2)

===Sorted Dictionaries
d1 = {'Smith': 43, 'James': 32, 'Edwards': 36, 'Cramer': 29}
•Dictionaries are unorderedand cannot be sorted
•d1.keys() or d1.values() can be sorted
sorted(d1.keys())   # ['Cramer', 'Edwards', 'James', 'Smith']
sorted(d1.values()) # [29, 32, 36, 43]

•Sorting by keys but returning the values:
list3 = [value for (key, value) in sorted(d1.items())]   #[29, 36, 32, 43]

===Task1-6
In file count the number of occurrences of words & Print top 100 words (5 letters or more) that occur the most

word_dict = {}
for line in open('alice.txt',encoding='utf8'):
    words = line.strip().split()
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

sortedwords = sorted(word_dict.items(),key=lambda rec:rec[1],reverse=True)
print(sortedwords)
five_letter=[(word,count) for word,count in sortedwords if len(word) >= 5]
print(five_letter[:100])
-------
from collections import defaultdict

word_dict = defaultdict(int)
for line in open('alice.txt'):
    words = line.strip().split()
    for word in words:
        word_dict[word] += 1
        # if word in word_dict:
        #     word_dict[word] += 1
        # else:
        #     word_dict[word] = 1

sorted_list = sorted(word_dict.items(), key=lambda one_rec: one_rec[1])
five_letters_or_more = [(key, val) for key, val in sorted_list if len(key) >= 5]

print(five_letters_or_more[-1:-100:-1])


===========Chapter 2 =====================
slide 83
===Exception Handling Structure
•Exceptions are handled using the try -except mechanism
try:
unsafe code
except 	exception1 as e1:
	exception1 handling
except exception2 as e2:
	exception2 handling
else:
	rare to use, perform if
	try block is successful
finally:
	always perform

---Alternate version without except
try:
    unsafe code
finally:
    always perform
-----------
a = input('Number 1: ')
b = input('Number 2: ')
try:
result = float(a) / float(b)
print('Division result is: {0}'.format(result))
except ValueError:
print('Improper value entered.')
---------------
a = input('Number 1: ')
b = input('Number 2: ')
try:
print('Division result is: {0}'.format(float(a) /float(b)))
except ValueError:
	print('Improper value entered.')
except ZeroDivisionError:    #Zero causes ZeroDivisionError, hits the second except block
	print('Number 2 may not be zero.')
-----------
a = input('Number 1: ')
b = input('Number 2: ')
try:
	result = float(a) / float(b)
	print('Division result is: {0}'.format(result))
except (ValueError, ZeroDivisionError):
	print('Improper value entered.')
------------
a = input('Number 1: ')
b = input('Number 2: ')
try:
	result = float(a) / float(b)
	print('Division result is: {0}'.format(result))
except Exception:   #Legal, but as a rule of thumb, try to handle the morespecific exception type and avoid the generic usage shown here
	print('Improper value entered.') 
------------
a = input('Number 1: ')
b = input('Number 2: ')
try:
	result = float(a) / float(b)
	print('Division result is: {0}'.format(result))
except Exception as err:
	print(err, type(err))

=====Working with Files
•Use the built-in open() command to work with files
	-Default mode is 'rt' (read text)
	-We specify the encoding because the default encoding is platform-specific
        -encoding  is new option in  python3
# read text
file = open(filename, encoding='utf8')
# write text
file = open(filename, 'w', encoding='utf8')
mode = 'r' or 'w' or 'r+' or 'a'(read, write, read+write, or append)
f = open('myfile.txt')  # f is a file object
entire_file= f.read()   #String containing entire file contents

f.readline()          # reads one line from a file, retains newline
f.readline(10)        # reads first 10 characters from the line    
list = f.readlines()  # reads all lines, puts them in a list       
f.writelines(list)    # writes a list, one item per line to a file 
-------------
for line in open('myfile.txt', encoding='utf8'):
	process(line)    # line will include the termination character (\n) 
-------------
try:                   
f = open('my_file.txt')    #If file is not found, open() fails, f will be None, therefore close()can't be called, so a nested try-finally structure is required                          
try:                   
	for data in f:         
	# work with data       
finally:               
	f.close()              
except IOError as e:    
  print(e)  

OR
f = None                            
try:                   
	f = open('my_file.txt')
	for data in f:         
		# work with data       
except IOError as e:    
	print(e)               
finally:               
	if f:                  
		f.close()    

•We always want to properly clean up when working with files
–Also true for many other resources, such as: database and network connections, sockets, etc.
•The following is a common programming paradigm:
do some initialization
do some work
do some cleanup

=======•with is a control structure that performs the following:
do some initialization
do work
do some cleanup
–Requires a context manager object to be supplied
withcontextmanageras obj:
do_work
--A context manager is a special object that defines how to initialize at the beginning and clean up afterwards

•The file object can be used in a with control
–It is a context manager because it has an__enter__() and __exit__() method defined
lines = []
try:
    with open('alice.txt') as f:
        lines = f.readlines()
except IOErroras e:
    print('Handled {0}'.format(e)) 
  
print('{0} lines read.'.format(len(lines)))

===Under the Sheets: How 'with' Works
•Context managers are objects that define two methods: __enter__and __exit__
•__enter__is always called at the beginning
–Return value becomes the optional 'as' object
•__exit__is called no matter what happens
class CtxMgr(object):
    def__enter__(self):
        print('enter')
        return 'foo'
    def__exit__(self, typ, value, traceback):
        print('exiting')
        
with CtxMgr() as obj:
    print(obj)
Outputs:
enter
foo
exiting
-------------------
===Multiple Contexts
•Python 3 supports multiple context managers within a single 'with' control:

filename, outfile= 'alice.txt', 'alice_out.txt'
try:
	with open(filename)as f_in, open(outfile, 'w')asf_out:
		for line in f_in:
		  f_out.write(line)
except IOError as e:
	print(e)

with open(outfile) as f:
	print(len(f.readlines()))

===Writing to Text Files
•In write'w' mode, use the file's write()method
–write()accepts a string that should end with \n
–Python will translate \n into a platform-specific line termination character

data = ['Lorem ipsum dolor sit amet, consectetur',...
'qui officiadeseruntmollitanimid estlaborum.',]

try:
  with open('data.txt', 'w', encoding='utf8') as f:
   for line in data:
     f.write('{0}\n'.format(line))
except IOErroras e:
   print(e)



===•Format values according to the user's locale:
import locale
locale.setlocale( locale.LC_ALL, "")
	Sets the locale for to the user’s default setting (typically found in the LANGenvironment variable)

locale.currency( 223471113.18, grouping=True )    # $223,471,113.18


===Print Formatting
•The print function has the following syntax:
print(val1, val2, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
	#sep = String inserted between values
	#end= defines a string appended to the end of the string
	#file= Defines where output will be sent
	#flush= Force flush the stream buffer
	
python 2  
	string is ascii mode 
    
python 3  
   string is unicode based
   print is a full function , should () always
   
-----------------------------------------------
===Task2-1
---•Write a program to find the top 10 baseball salariesfor a specified input year (1985 -2015)
===Logic 1------------------------------------------
import locale
import os.path
from collections import namedtuple

locale.setlocale(locale.LC_ALL, '')
working_dir = '../resources/baseball/'
master_filename = 'Master.csv'
salaries_filename = 'Salaries.csv'
results_filename = 'results.txt'

input_year = 0
salaries = []
players = {}
top_sals = []
SalaryRecord = namedtuple('SalaryRecord','playerid salary  year')
#input_year = input('Enter year (1985 - 2015): ')
input_year = 1985
try:
    with open(os.path.join(working_dir, salaries_filename), encoding='utf8') as f_sal:
        f_sal.readline()  # just read first line of column headings in .csv
        for line in f_sal: # starting to read from 2nd line
            record = line.strip().split(',')
            year, _, _, playerid, salary = record
            if int(year) == input_year :
                try:
                    salaries.append(SalaryRecord(playerid, int(salary), year))
                except ValueError:
                    pass
except IOError as err:
    print('Error   reading salary info '.format(err))
    sys.exit(42)
try:
    with open(os.path.join(working_dir, master_filename), encoding='utf8') as f_mast:
        for line in f_mast:
            record = line.strip().split(',')
            playerid, first, last = record[0], record[13], record[14]
            players[playerid] = (first, last)
except IOError as err:
    print('Error   reading master file  '.format(err))
    sys.exit(42)
salaries.sort(key=lambda record: record.salary, reverse=True)
with open(results_filename, 'w', encoding='utf8') as f_out:
    heading = '{0:30} {1:<20}  {2:<8}'.format('Name', 'salary', 'year')
    print(heading, file=f_out)
    print(heading)
    for record in salaries[:10]:
        playerid = record.playerid
        name = ' '.join(players[playerid])
        salary = locale.currency(record.salary, grouping=True)
        output = '{0:30}  {1:<20} {2:<8}\n'.format(name, salary, record.year)
        print(output, file=f_out)
        print(output)
====Logic 1  end -----------------------------
====Logic 2 -----------------------------------
import locale
import os.path


locale.setlocale(locale.LC_ALL, '')

working_dir = '../../resources/baseball/'
master_filename = 'Master.csv'
salaries_filename = 'Salaries.csv'
results_filename = 'results.txt'

input_year = 0
salaries = []
players = {}
top_sals = []


def salary_sort(sal_record):
    """
        Used for the key= parameter to sort the player-salary data by salary
        :param sal_record: string value representing a players salary
        :return: integer value for the salary
    """
    salary = 0
    try:
        salary = int(sal_record[4])
    except ValueError:
        pass

    return salary

#
#  Step 1.
#  Obtain the user's input, disallow non-int values or an empty selection
#
while True:
    input_year = input('Search salaries for what year?--> ')
    try:
        input_year = int(input_year)
        break
    except ValueError:
        print('Invalid year, try again.')

#
# not a requirement, but this allows option to choose how many records to return
#
num_records = 10
try:
    num_records = int(input('Number of records to retrieve (def.=10): '))
except ValueError:
    print('Retrieving 10 records.')


try:
    # Steps 2 & 3.
    # open and read data from both files
    #
    with open(os.path.join(working_dir, salaries_filename)) as file_sal, \
         open(os.path.join(working_dir, master_filename)) as file_mast:
        for line in file_sal:                                               # get each salary record
            sal_record = line.strip().split(',')
            try:
                record_year = int(sal_record[0])
                if record_year == input_year:
                    salaries.append(sal_record)                                     # load it into a list
            except ValueError:
                pass

        for line in file_mast:                                              # get each player record
            mast_record = line.strip().split(',')
            players[mast_record[0]] = mast_record                           # load it into a list

        # Step 4
        salaries.sort(key=salary_sort, reverse=True)                        # sort the salary records in descending order according to salary

        for top_sal in salaries:
            year = 0
            try:
                year = int(top_sal[0])                                  # get the year for each salary record
            except ValueError:
                pass

            # Step 5.
            playerid = top_sal[3]                                       # get the player's id, salary, year
            salary = top_sal[4]
            player_data = players.get(playerid)                         # get the player's name data from the other file data structure
            if player_data:                                             # checks if the player has data in the players dictionary, if not, we ignore them
                first_name = player_data[13]
                last_name = player_data[14]
                top_sals.append([first_name, last_name, salary, year])  # create a list of the player's relevant data
                if len(top_sals) == num_records:                        # stop after 10 records
                    break
except IOError as e:
    print('Error: {0}'.format(e))


#
#   Step 6. Write the results to a file
#
try:
    with open(results_filename, 'w', encoding='utf8') as f_out:         # write the results to a file
        f_out.write('Results\n')
        f_out.write('{0:<40} {1:<20} {2:<8}\n'.format('Name', 'Salary', 'Year'))
        for player_data in top_sals:
            name = ' '.join(player_data[0:2])
            salary = locale.currency(int(player_data[2]), grouping=True)
            year = player_data[3]
            f_out.write('{0:<40} {1:<20} {2:<8}\n'.format(name, salary, year))
except IOError as e:
    print(e)


# Testing the results
try:
    with open(results_filename) as f_test:                              # read the results back to verify them
        for line in f_test:
            print(line.rstrip())
except IOError as e:
    print(e)
====Logic2 end ---------------------------------------------------
def get_search_year():
    """ obtain the user's input, disallow non-int values or an empty selection"""
    input_year = 1985
    while True:
        input_year = input('Search salaries for what year?--> ')
        try:
            input_year = int(input_year)
            break
        except ValueError:
            print('Invalid year, try again.')

    return input_year

print (get_search_year())
------------
def get_record_count():
    """  Returns number of records to search for """
    num_records = 10
    try:
        num_records = int(input('Number of records to retrieve (def.=10): '))
    except ValueError:
        print('Retrieving 10 records.')

    return num_records
print(get_record_count)
--------------------
 

===Templating Mechanisms
•Templating provide a means for transforming data into 
another format (usually text formats such as HTML, XML, vCard)

import string 
records = [('cow', 'moon'),('dolphin', 'highwire'),('stuntman', 'bus')] 
tmpl= string.Template('The ${animal} jumped over the ${item}.')
for record in records:
	print(tmpl.substitute(animal=record[0], item=record[1]))
	
===•A popular 3rdparty templating tool is Jinja2
		#  Jinja2 supports 2.6, 2.7, 3.3+
from jinja2 import Template
records = [('cow', 'moon'),
('dolphin', 'highwire'),
('stuntman', 'bus')]
tmpl=Template('The {{animal}} jumped over the {{item}}.')
for record in records:
	print(tmpl.render(animal=record[0], item=record[1]))
	
---Jinja2 Scripting
<html>
	<body>
		{% for record in records %}
			<p>The {{record[0]}}jumpedover the {{record[1]}}.</p>
		{% endfor%}
	</body>
</html>
ch02_files_flow_control/templates/example_tmpl.jinja

from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateError, TemplateNotFound
env = Environment(loader=FileSystemLoader('./templates'))


try:
	tmpl= env.get_template('example_tmpl.jinja')
	print(tmpl.render(records=records))
except (TemplateNotFound, TemplateError) as e:	
	print('Error: {0} {1}'.format(type(e), e))

====Installing 3rdParty Tools: pip
•Jinja2 is an external module that must be installed before using it
•Most packages can be installed using a special tool called pip(python package installation tool)
	pip installs into <PYTHON_HOME>/Scripts (on Windows) 
	or the bin directory (on OS X or Linux)
	
•To use pip:
pip install package # pip install Jinja2
python -m pip install package  # another way to run pip	
pip uninstall package
pip3.6 install package  # pip3.6 install Jinja2
Python 3.6 already has pip installed, you may have to create a shortcut/alias for it.

===What Is PyPI?
–PyPiis the Python Package Index Repository
–Contains 3rdparty resources
•Sometimes called the CheeseShop(named after a Monty Python skit)
http://pypi.python.org/pypi
pip search package # pip searchJinja2



===Salaries Rendered as HTML
•Revisiting the baseball exercise--this time output will be an HTML pagerendered using Jinja2
–A Jinja2 HTML template is used to render the table: 
     ch02_file_flow_control/templates/baseball_stats.jinja
try:
	tmpl= env.get_template('baseball_stats.jinja')
	results = tmpl.render(records=top_sals)
	with open(results_filename, 'w', encoding='utf8') as f:
        f.write(results)
except (TemplateError, TemplateNotFound, IOError) as e:
	print('Error: {0}, {1}'.format(type(e), e))
import webbrowser
webbrowser.open(results_filename)

	
    
	
=============7 feb 2018  wednesday=========================

7 feb 2018  wednesday
slide 113 on pdf 
Function Definitions
•Functions provide a means to write reusable code
collections.namedtuple.__doc__  --> give the documentation of namedtuple function
–Python affords powerful features to functions 
deffunc_name(arg0, arg1, arg2, ..., argN):
	statements
	return value
	#Function statements must be indented
	#Return values are optional. A value of 'None' is returned when a return statement is omitted
	#List of parameters must be supplied or () if none


===Calling Functions
•Functions must be defined before they can be called
defdisplay_results(customer, purchase_amount):
	print('Customer: {first} {last}, amount: ${p_amt:,.2f}'.format(first=customer['first'],
			last=customer['last'],
			p_amt=purchase_amount))	
cust= {'first': 'James','last': 'Smith'}
display_results(cust, 1108.23)			

--Using Default Arguments
def convert_file_size(filesize, precision=1, override=None):
	# details of this function are not relevant

print(convert_file_size(12))# 0 KB
print(convert_file_size(1200))# 1.2 KB
print(convert_file_size(1200, 3, 'MB'))# 0.001 MB
print(convert_file_size(12000000000))# 11.2 GB
print(convert_file_size(12000000000, 2, 'TB'))# 0.01 TB
print(convert_file_size(12000000000, 2, 'KB'))# 11,718,750 KB

--Keyword Arguments
•All functions support keyword parameters
–Function calls become more flexible using this technique
def  convert_file_size(filesize, precision=1, override=None):
	# details not shown ...
All of these would be valid calls:
convert_file_size(1200)
convert_file_size(1200, 3, 'MB')
convert_file_size(1200, precision=3, override='MB')
convert_file_size(filesize=1200, precision=3, override='MB')
convert_file_size(precision=3, override='MB',filesize=1200)
convert_file_size(override='MB',filesize=1200)

---Multiple Positional Arguments
•To define a function in which the number of parameters to it are unknown, use the (*) character:
def display_info(name, age, spouse, *children):
	print(name, age, spouse, children)
display_info('Bob', 37, 'Sally', 'Timmy', 'Johnny', 'Annie')
	#Bob 37 Sally ('Timmy', 'Johnny', 'Annie')
	
---Multiple Keyword Arguments
–Results are placed into a dictionary
def display_info(**family):
	print(family)
	
display_info(name='Bob', age=37, spouse='Sally',child1='Timmy',  child2='Johnny', child3='Annie')
  # output = {'child1': 'Timmy', 'child2': 'Johnny', 'child3': 'Annie', 'name': 'Bob', 'age': 37, 'spouse': 'Sally'}

---Mixing Positional and Keywords
def  display_info(*args, **kwargs):
	print(args, kwargs)
display_info('hello', 10, ['stuff1', 'stuff2'],item1='value1', foo='bar')	

	#('hello', 10, ['stuff1', 'stuff2']) {'item1': 'value1', 'foo': 'bar'}
--print()  function is example of using positional and keyword arguments
---Unpacking Arguments
•In a function definition, *and **'collect' values
•These symbols may also be used in the function call
–Values are dispersed, or 'spread out' in the function def
–It works the opposite as it does in the function declaration

def display_results(customer, purchase_amount):
print('Customer: {first} {last}, amount: ${p_amt:,.2f}'
.format(p_amt=purchase_amount, **customer))
		# Customer is a dictionary, so using ** on the dictionary in the function call will cause the dictionary to be 'expanded' into keyword arguments supplied to this function.
cust= {'first': 'James','last': 'Smith'}
display_results(cust, 1108.23)



---Introducing Modules
• Modules are namespaces in Python
– Physically, each .py file represents a module
– Functions, variables, classes declared at the top of a
module can be made available to other modules
– These attributes must be imported before being used
• Most modules of Python's standard library are found in the <PYTHON_HOME>/Lib directory
import <moduleName>
from <moduleName> import <attributes>
from <moduleName> import <attributes> as <alias>

import os
import sys
print(os.environ, sys.path)
• What's in a module?
dir(module_name)   #  Identifies contents of a module
help(module_name)
---Adding Your Own Modules
•Python programs locate modules by looking at the sys.path variable
•To ensure sys.path"sees" your modules, perform one of these:
1.Modify sys.path directly
	sys.path.append('/home/modules')
2.Put your modules in the <PYTHON_HOME>/Lib/site-packages
3.Create an OS-level environment variable called PYTHONPATH
---Variable Scope
•Accessing variables within Python follow the acronym LEGB
global_x= 10
def change_global_x():
	global_x= 20     #You might expect this to change the global_x, but it doesn't
	
change_global_x()
print(global_x)   # 10

•To modifythe global variable use the globalkeyword
global_y= 10
def change_global_y():
	global global_y
	global_y= 20
		
change_global_y()
print(global_y) # 20

•A built-in function calledglobals()returns a dictionary of available global vars
#{'__doc__': None, '__spec__': None, '__builtins__': <module 'builtins' (built-in)>, '__package__': None, '__cached__': None,'x': 10, '__name__': '__main__', '__file__': 'student_files/ch03_functions/06_assigning.py', 'change': <function change at 0x0000000002602400>}
x = 10
def change():
	print(globals())
	globals()['x']= 20
change()
print(x)   # 20

•Immutable values passed to a function are passed by value while mutable values are passed by reference
def change_me(lst, tup, scalar):
	scalar += 
	1lst*= scalar
	tup*= scalar
	print(lst, tup, scalar)  # [1, 2, 3, 1, 2, 3] (4, 5, 6, 4, 5, 6) 2
	
scalar = 1
lst= [1, 2, 3]
tup= (4, 5, 6)
change_me(lst, tup, scalar)
print(lst, tup, scalar)     # [1, 2, 3, 1, 2, 3] (4, 5, 6) 1

--------------------
x1=10
x2=15
def check():
    global x1
    print('in function',x1)
    x1 = 20
    print(globals())
    globals()['x2']=25

check()
print(' in main x1= ',x1,'x2 =',x2)

====================================================================


=============Chapter 4 =====================
slide 133 of pdf
Why Classes?
•Earlier we introduced named tuples
	from collections import namedtuple
	Contact = namedtuple('ContactRecord', 'first last age email')
	c = Contact('John', 'Smith', 43, 'jsbrony@yahoo.com')
•Limitations include:
–Inability to easily modify data: it is effectively a tuple
–Operations on this data are maintained separately
Classes create (instantiate) objects
–Object data not only can be modified, but can use the behaviors (methods) defined in the class

class Contact:
	""" Defines a Contact type """
	def__init__(self, name='', address='', phone='', email='',company='', position=''):
		self.name = name
		self.address = address
		self.phone= phone
		self.email= email
		self.company= company
		self.position= position
		
	def__str__(self):
		return '{0}'.format(self.name)

c = Contact('John Smith', '123 Main St.', '(970)322-9088','jsmith433@yahoo.com', 'Acme Inc.',
'Rubber Hole Engineer')

c.alt_email= 'jsmith433@gmail.com'
print(c.name, c.alt_email)
print(c, type(c))  # John Smith <class '__main__.Contact'>
		
===Constructors
class Contact:
def  __init__(self, name='', address='', phone='', email='',company='', position=''):
	# self must always be defined as the first argument in the constructor
	self.name = name
	self.address = address
	...
c = Contact('John Smith')
#Creating instances executes the constructor

---Adding Methods & the self Parameter
class Contact:
	def__init__(self, name='', address=''):
		self.name = name
		self.address= address
		
	def display_columned(self, nw=20, aw=25):
		return '{0:<{nw}} {1:<{aw}} '.format(self.name,self.address, nw=nw, aw=aw)
		
	def__str__(self):
		return '{0} {1}'.format(self.name, self.address)
	__repr__ = __str__
	
c = Contact('John Smith', '123 Main St.')
print(c.display_columned())
	#Instances may invoke the methods defined in the class, 
	but you should not specify self in the call
	
---Using the Class & Magic Methods
class Contact:
	...(as previously defined)...
from modules.contacts2 import Contact
contact_list= []
try:
	with open('../resources/contacts.dat') as f:
		for line in f:
			contact_data= line.split(' ')
			name, address = contact_data[:2]
			contact_list.append(Contact(name, address)) #Instantiate one contact per record
except IOErroras e:
	print('Error: {0}'.format(e))
print(contact_list) 
#[Bob Green, Sally Smith, John Brown, Ed Parker]  
#Printing the entire list causes a nice output because __repr__ = __str__
	

---Instances Usually Backed by Dictionaries
•Most instances have a __dict__property that allow instances to be accessed using dictnotation
c = Contact('John Smith', '123 Main St.', 
	[{'work':'(970)322-9088', 'home':'(970)455-2390'}],
	'jsmith433@yahoo.com', 'Acme Inc.', 'RubberHammers')
print(c.__dict__['name'])
•Dictionary-backed objects can alternatively use
vars():
c.__dict__ is similar to vars(c)
#When working with namedtuplesas dictionaries, version 3.4.3 and later (as well as 2.7.5 and later) should use _asdict()instead of vars().

---Defining Properties
class Contact:
	def__init__(self, name='', address='', email='', ...):
		self.name= name
		self.address= address
		self.email= email
		...
		
	@property
	def name(self):
		return self._name

	@name.setter
	def  name(self, name):
		self._name= name

#•Properties are Python's version of getters and setters
#Use @property to define a method that can act like a getter
#@prop.setteris the syntax to define a setter
	
	@property
	def email(self):
		return self._email
		
	@email.setter
	def email(self, email):
		if '@' not in email:
			self._email= ''
		else:
			self._email= email
-•The@ syntax describes a decorator
-The "private" property is set in the setter

•Use the properties as if they were typical attributes
–Performing assignments will execute the setter method
	c = Contact()
	c.name= 'Bob'  # Invokes name() setter
	c.email= 'bob@yahoo.com'  #Invokes email() setter
	print(c, c.email)  # Invokes email() getter
-----------------------------------
class player:
    def __init__(self, fname='',lname= ' ',salary =0,playerid=''):
        self.first_name=fname
        self.last_name=lname
        self.salary=salary
        self.playerid=playerid
    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
    @property
    def first_name(self):
         return self._first_name
    @first_name.setter
    def first_name(self,fname):
        self._first_name=fname
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,salary):
        self._salary=0
        if salary > 0:
              self._salary=salary

play1 = player('boby','joseph',3000,10)
print(play1,play1.salary)
	
========================================================
8 feb 2018

Class Attributes
•Variables created at the class level are called class attributes
–They should be modified via the class:

class RaceCar:
	MAX_SPEED = 24
	ACCELERATION = 5
	
	def__init__(self):
		self.speed= 0
		
	def accelerate(self):
		self.speed+= RaceCar.ACCELERATION
		if self.speed> self.MAX_SPEED:
			self.speed= self.MAX_SPEED
#Class attributes can be accessed by both the Class AND the instance, 
but should not be modified by the instance
--Note: do not try to modify ACCELERATION through the instance:
self.ACCELERATION= 10 would be inappropriate

====Static Methods
---Python defines static methods using the @staticmethoddecorator
import urllib.request
from urllib.errorimport URLError

class Page:
	@staticmethod
	def page_load(url):  #Do not specify self , Call is accomplished directly via Classname.methodname()
		try:
			with urllib.request.urlopen(url) as f:
				results = f.read().decode()
		except URLErroras e:
			results = 'Error: {0}'.format(e)
		
		return results
webpage = 'http://cisco.com'
print(Page.page_load(webpage))

====Inheritance: Classic Constructor Call
class Contact:
	def__init__(self, name='', address='', phones=None):
		self.name = name
		self.address= address
		self.phones= phones
	
	def __str__(self):
		return '{name} {address} {phones}'.format(**self.__dict__)
		
class BusinessContact(Contact):
	def __init__(self, name='', address='', phones=None, email='', company='', position=''):
		Contact.__init__(self, name, address, phones)  #Calls the base class constructor
		self.email= email
		self.company= company
		self.position= position
		
positionbc= BusinessContact('John Smith', '123 Main St.',
{'home': '(970)455-2390'})
print(bc)

---Using super() -Preferred
class Contact:
	def__init__(self, name='', address='', phones=None):
		self.name = name
		self.address= address
		self.phones= phones
	
	def__str__(self):
		return '{name} {address} {phones}'.format(**vars(self))

class BusinessContact(Contact):
	def__init__(self, name='', address='', phones=None, 
			email='', company='', position=''):
		super().__init__(name, address, phones)
		self.email= email
		self.company= company
		self.position= position
		
bc= BusinessContact('John Smith', '123 Main St.',{'home': '(970)455-2390'})
print(bc)

==================

*********************************************************************************************
chapter5
=====Introducing the Python Standard Lib
•The Standard Library contains over 200 modules of functions and classes
•Documentation:
	https://docs.python.org
	https://docs.python.org/3/library/index.html

•Use dir()within an interactive shell to view top-level properties of an object or module
>>> dir(sys)
['__displayhook__', '__doc__', '__excepthook__', '__name__', '__package__','__stderr__',
 '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', '_getframe', 'api_version',
 'argv', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats',
 
•The sys module includes resources for monitoring the Python interpreter environment:
sys.path    list of directories the interpreter uses to locate modules
sys.modules dictionary of all loaded modules and their file locations
sys.argv    list of command line arguments starting with the file name
sys.builtin_module_names  tuple of strings identifying all pre-compiled modules (no .pyfile exists for these)
sys.exit(exit_value)   exits the program with an optional exit value
sys.stdin
sys.stdout

sys.stderr    file objects that reference the standard streams
sys.version   gives information about the Python version used
sys.exc_info()  gives type, value, tracebackinforfor a current exception
sys.getrefcount(obj)   number of references to an object (will always be 1 high)

====sys Module Example: A whichModule Utility
import importlib
import sys

defwhichmod(modules):
	for module in modules:
		if module in sys.builtin_module_names:
			print('{module} built in'.format(module=module))
		else:
			try:
				module = importlib.import_module(module)
				location = module.__file__
				print('{loc}'.format(loc=location))
			except (ValueError, ImportError):
				print('{module} not found'.format(module=module))
				
module_names= input('Module name(s) [separated by spaces]: ')
modules = module_names.strip().split(' ')

if len(modules[0]) < 1:
	modules = ['os', 'sys', 'string', 'subprocess',
				'Customers', 'parser', 'foo']
				
whichmod(modules)

==== osModule
•The osmodule provides access to many operating system services

os.name  -string yielding the name of the operating system (e.g. 'nt')
os.environ  -a dictionary of osenvironment variables
os.sep  -path separator character (e.g. semi-colon on windows
os.pathsep -path separator character (e.g. semi-colon on windows ';')
os.linesep -platform specific end of line character (e.g. semi-colon on windows '\r\n')
os.chdir(dir_path)-changes to a specified directory
os.listdir(dir_path)-lists the contents of a particular directory
os.walk(directory)-powerful function that returns directory and file information. 
			It traverses an entire subtree in a directory structure.
os.path  -name of the osspecific module for additional processing. 
		 This module contains many additional functions for working with OS paths.
		 
os.getcwd()	-get the current working directory
os.getenv(envVariable, default) -returns an environment variable
os.rename(old, new)	-rename a file or directory
os.remove(filepath)	-removes a file (errors on directories)	
os.rmdir(path)-remove a directory
os.removedirs(path)-recursively remove all directories
os.chdir(path)-change to a new directory
os.mkdir(dir)-make a directory
os.makedirs(dirs)-make all specified directory levels
os.listdir(path)-return a list of files in a dir
os.path.isfile(file)-checks whether item is a file
os.path.isdir(dir)-checks whether item is a directory
os.path.exists(path)-checks for existence of a file or dir
os.path.basename(path) -returns only the last path level
os.path.join(path1, path2, ....)-smartly joins paths
os.split(path)-returns a head and tail where tail is only the last part of a path
os.walk(path)-walks all files and dirsof a path	 
		 
======os.stat()
import os
import time
stats = os.stat('./os_stat.py')	 #os.stat(filename) -returns statistics on a file or path
print(stats.st_size)
print(stats.st_atime)
print(time.ctime(stats.st_atime))  #Sun Feb 22 19:59:17 2018

print(time.strftime('%m-%d-%Y', time.localtime(stats.st_atime)))
print(stats)

os.stat_result(
st_mode=33206,   #File permissions bits
st_ino=39687971717207165,  # inode
st_dev=2150466117,  #device
st_nlink=1,
st_uid=0,
st_gid=0,
st_size=57,   #filesizein bytes
st_atime=1424652882,  #Last access time, mod time, creation time in secs.
st_mtime=1424652882,
st_ctime=1423761797
)


	 
		 
====time Module
	

====datetimeModule
•The datetimemodule defines a date, time, and datetimeclass for encapsulating specific dates
-date 
year
month
day

-time
hour
minute
second
microsecond
tzinfo

-datetime
year
month
day
hour
minute
second
microsecond
tzinfo

import datetime
now1 = datetime.datetime.now()# current date & time
now2 = datetime.date.today()# current date
print(now1, now2)

d = datetime.date(2009, 1, 1)
print(d.year, d.month, d.day)
print('formatted using strftime: {fmt}'.format(fmt=d.strftime('Day %d of %B, Day %j in %Y, ')))

====csv Module
•The CSV module simplifies working with csv files:
import csv
airports=[]
try:
	with open('../resources/airports.dat', encoding='utf8') as f:
		try:
			for row in csv.reader(f):
				airports.append(row)  #row represents a list of strings from one line within the file
		except csv.Erroras e:
			print('Error: {err}'.format(err=e))
except IOErroras e:
	print(e)
	
try:
	with open('first100.dat', 'w', encoding='utf8') as f:
		try:
			csv.writer(f).writerows(airports[1:101])
		except csv.Erroras e:
			print('Error: {err}'.format(err=e))
except IOErroras e:
	print(e)
	
	






===========chapter 7=======================
Regular  expression
•Python supports Perl-style regex's via the remodule
•Module-level methods include:

match(pattern, string, flags) -from the beginning, return Match object if a match exists, None otherwise
search(pattern, string, flags) -search entire stringfor match, return Match object if exists, None otherwise
findall(pattern, string, flags)-list of matches of patterns within string
finditer(pattern, string, flags)-iterator of matches of patterns in string
fullmatch(pattern, string, flags)-apply pattern to full string, Match object or None returned
split(pattern, string, maxsplit, flags)break string up by regex pattern
sub(pattern, repl, string, count, flags)find match, replace replwith it. Return new string.

•To avoid confusion by having to escape characters within a regex string, use raw strings:
matchobj= re.match('\\d{5}', '12345')
matchobj= re.match(r'\d{5}', '12345') #With raw strings, backslashes are not treated as special character

====Common Regexes
Symbol   Meaning
^	fromthe start
$	to the end
.	any character
\s	whitespace
\S	non-whitespace
\d	digit
\D	non-digit
\w	alphanumeric character
\W	non-alphanumeric character
\b	word boundary
\B	non-word boundary
*	0 or more
+	1 or more
?	0 or 1
{n}	exactly n
{5,8} 5 to 8
{5,}  5 or more
{,8}  Upto 8
(1|2|3)  1or 2or 3
[adrn]   a or d or r or n
[a-f]    oneof a thru f
[^def]   not d or e or f
[a-zA-Z] one of any letter

===Match Objects
•A Match object is returned from either match() or search()

matchobj= re.search('seven', speech)
if matchobj:
	print('seven found at pos: {0}'.format(matchobj.start()))
	
–Match object methods:
start()-index of the start of the match
end()-index of the end of the match
span()-both values (start, end)
groups()returns a tuple of all sub-groups (parenthesized expressions)
group(n)specified sub-group, zero is the whole match

•When a match occurs, matchobj.groups() will return a tuple of the whole match and any subgroups
–Use matchobj.group(n)to obtain the subgroup
matchobj= re.search(r'(\w+) (\w+) (\w+)',
		'Four score and seven years ago')
print(matchobj.groups()) # ('Four', 'score', 'and')
print(matchobj.group(0)) # Four score and
print(matchobj.group(1)) # Four
print(matchobj.group(2)) # score
print(matchobj.group(3)) # and

---Using findall()
•The findall() method allows for finding multiple occurrences of a regex
–Returns a list of strings that match
str_matches= re.findall(r'\w+', 'Four score and seven years ago')
print('How many words: {0}'.format(len(str_matches)))  #How many words: 6
print(str_matches)  #['Four', 'score', 'and', 'seven', 'years', 'ago']

---substitution
import re
word = 'hello-,.?????.\....\..?'
print(word)
#word = re.sub(r'([-,.?]|[??]|[..])','', word) # match symbols patten in [] on word and replace with  ''
#word = re.sub(r'[-\\?.,]{2}','', word.lower())# serach and repalce 2 occrance of symbol in [-\?.:;,!]
word = re.sub(r'[-\\?.,]{2,}','', word.lower())#  repalce 2 or more occrance of symbol in [-\?.:;,!] and replace ''
#word = re.sub(r'([-,.\\?{2,}])','', word)
print(word)
===============================================================
========XML=====================================================

# stats.py (from our task4-1 exercise), this goes in ch04_oo/task4_1/support directory
from collections import namedtuple
import locale
import lxml.etree as etree
from lxml.etree import ElementTree
from lxml.etree import Element
import sys

locale.setlocale(locale.LC_ALL, '')


class Player(object):
    def __init__(self, first, last, salary, year):
        self.first = first
        self.last = last
        self.salary = salary
        self.year = year

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = 0
        if salary > 0:
            self._salary = salary



def get_year():
    """Gets the year from user input"""
    return input('Enter year (1985 - 2015): ')


def retrieve_data(year_input, salaries_filepath, master_filepath, num_records=10):
    players = {}
    salaries = []
    top_sals = []
    SalaryRecord = namedtuple('SalaryRecord', 'playerid salary year')

    try:
        with open(salaries_filepath, encoding='utf8') as f_sal:
            for line in f_sal:
                record = line.strip().split(',')
                year, _, _, playerid, salary = record
                if year == year_input:
                    try:
                        salaries.append(SalaryRecord(playerid, int(salary), year))
                    except ValueError:
                        pass
    except IOError as err:
        print('Error reading salary information: {0}'.format(err))
        sys.exit(42)

    try:
        with open(master_filepath, encoding='utf8') as f_mast:
            for line in f_mast:
                record = line.strip().split(',')
                playerid, first, last = record[0], record[13], record[14]
                players[playerid] = (first, last)
    except IOError as err:
        print('Error reading master file: {0}'.format(err))
        sys.exit(42)

    salaries.sort(key=lambda record: record.salary, reverse=True)

    for record in salaries[:num_records]:
        top_sals.append(Player(players[record.playerid][0], players[record.playerid][1],
                               record.salary, record.year))

    return top_sals


class PrintReportException(Exception):
    def __init__(self, message):
        self.message = message


def print_report(data, columns, results_filename='results.txt'):
    try:
        with open(results_filename, 'w', encoding='utf8') as f_out:
            heading = '{0:30}{1:<20}{2:>12}'.format(*columns)
            print(heading, file=f_out)
            print(heading)

            for player in data:
                name = ' '.join([player.first, player.last])
                salary = locale.currency(player.salary, grouping=True)
                output = '{0:30}{1:<20}{2:>12}'.format(name, salary, player.year)
                print(output, file=f_out)
                print(output)
    except IOError:
        raise PrintReportException('Error writing report!')


def create_xml(data, xml_filename):
    root = Element('players')
    tree = ElementTree(root)

    for record in data:
        player = Element('player')
        first = Element('first_name')
        last = Element('last_name')
        salary = Element('salary')
        player.set('year', record.year)
        first.text = record.first
        last.text = record.last
        salary.text = '${0:,}'.format(record.salary)
        player.append(first)
        player.append(last)
        player.append(salary)
        root.append(player)

    with open(xml_filename, 'w', encoding='utf8') as f_out:
        f_out.write(etree.tostring(root, pretty_print=True).decode())
        print(etree.tostring(root, pretty_print=True).decode())

# task4_1_starter.py (driver), this goes in ch04_oo/task4_1 directory
import os

import ch04_oo.task4_1.support.stats as stats

working_dir = '../../resources/baseball/'
master_filename = 'Master.csv'
salaries_filename = 'Salaries.csv'
results_filename = 'results.txt'

year_input = stats.get_year()

top_sals = stats.retrieve_data(year_input, os.path.join(working_dir, salaries_filename),
                               os.path.join(working_dir, master_filename))

try:
    stats.print_report(top_sals, ['Name', 'Salary', 'Year'], results_filename)
except stats.PrintReportException as err:
    print('An error occurred while writing the report. {0} '.format(err))
stats.create_xml(top_sals, 'results.xml')


==============================================================
chapter 6  Network programming

Humbles, Ashley R.  (coordinator)
Crider, Brad J. , 
Dalal, Saroj S. , 
John Crews ,   
Lifeng Bian  ;  
Mark Feifarek ;  
Otieno, Willys  ,    Quantitative Analytics Cons
Sedani, Mayur M.  , , Technology Manager
Shane Biesemeyer  , 
Zhiyu  ;  
	
Dettler, Derek D., contact him to setup pyCharm in wellsF  laptop
Jim Meek  , 
Student Manual:
------------------------------
import sys
print(sys.version)

def my_func(greeting):
    print(greeting)

my_func('hello')
--------------------------
•Strings are immutable sequencesof Unicode characters
–Type: str
–Formal notation:my_str= str('Python is great!')
–Literal notation:my_str= 'Python is great!'


 –May use single or double quotes  (PEP-8 does not have a preference)
 -Triple quoted strings can span multiple lines. A common use is for documentation (called a docstring).
my_str= 'Python\'s great fun'
my_str= "Python is great fun"
my_str= """Python is so much fun"""

•Strings are sequences and therefore support random access:
my_str= 'Python is fun'
print(my_str[0]) # 'P'

•Sequences may be sliced (sub-sequenced):
slice = string[start : end : step]
-tartval(included)
-endval(excluded)
print(my_str[0:9]) # 'Python is'
print(my_str[:3]) # 'Pyt'
print(my_str[3:]) # 'hon is fun'
print(my_str[-1]) # 'n'
Tip:
copy = sequence[ : ]
makes a shallow copy

•Strings may be concatenated (creates a new string):
my_str= 'Python is '
new_str= my_str+'fun'
•Long strings may be continued:
my_str= 'I just cannot seem \
to finish this \
darn string!'
•Strings (sequences) may be replicated:
'hello' * 3  
  hellohellohello
•join()  ->Concatenates a list of strings using the specified separator string
	nums= ['1','2', '3']
	' '.join(nums)# 1 2 3


•split() ->Creates a list of strings based on a specifiedseparator string
	my_str= 'Python is great'
	my_list= my_str.split(' ')# Results: ['Python', 'is', 'great']

•replace()  -> Returns a new stringwith all matching substrings replaced by the new one
	my_str.replace('is', 'is still')# yields: 'Python is still great'

*strip()   ->  Returns a new string with whitespace removed from each end
	new_str= ' Whitespace will be removed. '.strip()
•find()  -> Finds the index of the first occurrence of the substring
	my_str= 'Python is great'
	my_str.find('is')# returns 7
	my_str.find('not')# returns -1
•str()  -> String class constructoraccepts any object returns a string object
	s = str(55)# creates a string from the int
	s = str(3.14)# creates a string from the float
•Use the type name as a function to perform conversions
	s1 = str(55)# '55'
	s2 = str(3.14)# '3.14'
	i1 = int('37')# 37
	i2 = int(3.14)# 3
	f1 = float(55)# 55.0
	f2 = float('3.14')# 3.14
•If a conversion cannot be made, a ValueErroris raised:
	int('hello')
	ValueError: invalid literal for int() with base 10: 'hello'

===String format()
•A preferredway to format data is to use the format() method of the string class
	s = 'It has been raining for {0}{1}and{0}{2}'
	new_str= s.format(40, 'days', 'nights')
	'It has been raining for 40 days and 40 nights'

	{ fieldname | index [!spec] [:format] }
	s6 = '{lang} is over {0:0.2f} {date} old.'.format(20, date='years', lang='Python')
		Python is over 20.00 years old.
	# format() examples:
	print('{0:>9}'.format('101.55'))  # 101.55 (field-width of 9, > right aligned, remaining space fill substitute character)
	print('{0:->9}'.format('101.55')) #  ---101.55  
	print('{0:-<9}'.format('101.55')) #  101.55---  ( < left aligned, remaining space fill substitute character)
	print('{0:-^20}'.format('hello')) # -------hello--------(^ is center aligned,field-width 20,fill - remaining space)

•Additional string class methods include:
capitalize()
center(width, char)
count(str)
endswith(str)
expandtabs()
index()
join(sequence)
ljust(width, char)
lower()
isalnum()
isalpha
isdecimal()
isdigit()
isidentifier()
islower()
isnumeric()
isprintable()
isspace()
istitle()
isupper()


Sequences
•Sequences are ordered collections of objects
	–Types include: str, list, tuple, range
	dirs= ['North', 'South', 'East', 'West']
•Common sequence capabilities:
–Random access, slicing
	dirs[2]# 'East'
	dirs[-2:]# ['East', 'West']
–Concatenation	
	dirs+ ['NW', 'NE', 'SW', 'SE']
–Replication
	dirs* 2 # ['North', 'South', 'East', 'West','North', 'South', 'East', 'West']
–Membership
	if 'east'.capitalize() in dirs:print(dirs.index('east'.capitalize()))

•Lists -mutable, ordered collections of objects
my_list= []
my_list= [1, 3, 5]
my_list= [3.3, 'hello', Person()]
my_list= list('hello')
my_list= [3.3, 'hello', Person(), 3.3, Person()]  #Lists may contain duplicates 
	
my_list= [1, 2, 3]
my_list.append(10)
my_list.insert(1, 'hello')    #1, 'hello', 2, 3, 10

===Tuples
•Tuples -immutable, ordered collections of objects
my_tuple= ()   #Empty tuple
my_tuple= (1, 3, 5)
my_tuple= (3.3, 'hello', Person())
my_tuple= tuple()   #Empty tuple
my_tuple= tuple('hello')  #tuple(sequence)
my_tuple= (1,)    #tuple with one element

my_list = [4, 5, 6]
t = (my_list, 2, 3)
t[0] = my_list2   ----> this will cuase error
print(t)

my_list = [4, 5, 6]
t = (my_list, 2, 3)
t[0].append(10)   --> is allowed , it adding to my_list in the tuple
print(t)

===Useful Sequence Functions
•len()
dirs= ['North', 'South', 'East', 'West']   
print(len(dirs), len(dirs[0]))  
  4, 5
•max()
	max([1973, 2001, 2015, 2013, 1994])  # 2015
•min()
	min([1973, 2001, 2015, 2013, 1994])  # 1973

===Illegal Operations
•The following operationsmay notbe performed on sequences:
[1, 2, 3] + 'Bob'
[1, 2, 3] + (4, 5, 6)  
      Can't concatenate different sequence types
my_list= []
my_list[0] = 'Bob'
	Empty list to begin with, so there is no 0thaddress to assign something into
my_list= [None] * 5
my_list[0] = 37
my_list[1] = 'Bob'
	This approach is legal because the list is sized to begin
 
===Control Structures
if test:
<one or more statements>
eliftest2:   #There may be zero or more elifbranches
<one or more statements>
else:    #The elseis optional
<one or more statements>

if test:
    print('This is part of the if block!')
    print('So is this!')
print('This is not!')
	Beginning and ending of blocks are determined by indentations (use 4 spaces)

===Truthy/ FalseyValues
  Test conditions in control structures expect a bool
       However, everything in Python can evaluate to a Trueor Falsevalue
These values are all considered False:
False
None
0
0.0
''
[]
()
{}
Everything else evaluates to True!
data = [1, 2, 3]
if len(data):
    print('Datanot empty.')
Comparison Operators
•Below are a few of the comparison operators that may be used in tests:
a == b
a < b
a > b
a >= b
a <= b
a != b
a is b (same object)
a is not b
a in y (a member of)
a not in y
not a
a and b(and, or both short circuit)
a or b

===Conditional Expressions (Ternary Operator)  
•Python has a version of a ternary operator:
	username = input('Enter username--> ')   #Prompts user for input returning a string after Enter key is pressed  
    is_valid= True if len(username) > 6 else False
        Sets is_validto Trueif conditional is True otherwise sets it to False  
===Iterative Control Structures  
while test:
	<one or more statements>  
else:
	<one or more statements>
       Optional else block is only executed if conditional terminates naturally (without a break)  
	elseblock not commonly used  

for one_itemin collection:
	<one or more statements>
else:
	<one or more statements>
	Optional else only executed if conditional terminates naturally

while True:
     name = input('Enter name: ')
     if not name:
         break
      process_name(name)
	This loops until just the Enterkey is pressed
	process_name()is just a user-defined function here




====Write a script that finds the domain nameof a URL
prefixes = ['http://', 'https://']
suffixes = [':', '/', '?']
urls = ['https://docs.python.org/3/',
        'https://www.google.com?gwrs_rd=ssl#q=python',
        'http://localhost:8005/contact/501'
        ]
print(urls)
for url in urls:
    for prefix in prefixes:
        if url.startswith(prefix):
            domain = url[len(prefix):]
    for suffix in suffixes:
        pos = domain.find(suffix)
        if pos != -1:
            domain = domain[:pos]
    print(domain)
====================================
Task 1-3
---program to count a word in files in given directory
import sys
import os

args = sys.argv                                                 # get command-line args
if len(args) != 3:
    print('Improper arguments provided. Syntax:')
    print('python task1_3.py wordexpression directory')
#    sys.exit(42)

wordexpression = args[1]
directory = args[2]

wordexpression = 'print'
directory = '..'
file_list = []

dir_contents = os.listdir(directory)

for entry in dir_contents:                                  # check each item if it is a file or not
    filename = os.path.join(directory, entry)
    if os.path.isfile(filename):
        file_list.append(filename)                          # add only files to the file_list


print(file_list)
for filepath in file_list:
    line_count = 0
    for line in open(filepath):
        line_count += 1
        filename = os.path.basename(filepath)
        if line.find(wordexpression) is not -1:
            print('File: {0}, Line: {1}, ({2})'.format(filename, line_count, wordexpression))
=====================================================

in pycharm  
   tools -> Python Console   =>  to get python console  in pycharm
in pycharm 
   highlight a function of module  then 
   view -> quick definition   (for help)
   view -> quick Documentaiton 
  
dir(os)     # it will give items in a  module
dir(os.path)  

help(os.path)
help(os.path.join)  # help on usage of the module


 

===More with Lists
•Useful list methods:
append(item)adds item to the end of the list
insert(pos, item)adds item at poslocation
index(item)finds the first occurrence or -1
sort()sorts in-place
extend(lst2)similar to list1 += list2
reverse()reverses the order of the list
pop()returns/removes last item
remove(item)removes first occurrence of item

===Additional Iterating Techniques
•Use enumerate() to obtain access to both the indexand the valuewhen iterating:
weekdays = [
'Monday','Tuesday',
'Wednesday','Thursday','Friday'
]  
for idx, value in enumerate(weekdays):
  print(idx, value)
0 Monday
1 Tuesday
2 Wednesday
3 Thursday
4 Friday
   # note index start at 0 if no starting point given

for idx , item in enumerate([5,8,11,13],20):
    print('index is {}; val is {}'.format(idx,item))
index is 20; val is 5
index is 21; val is 8
index is 22; val is 11
index is 23; val is 13

for ind, val in enumerate(range(-5, 5,3),-4):
    print('ind is {}; val is {}'.format(ind, val))
ind is -4; val is -5
ind is -3; val is -2
ind is -2; val is 1
ind is -1; val is 4

•Use reversed()to iterate from the end to start:
for value in reversed(weekdays):
    print(value)
Friday
Thursday
Wednesday
Tuesday
Monday

===Iterating Multiple Collections
•Another useful function to assist with processing lists in parallel is zip():
fruit= ['Apple', 'Orange', 'Banana', 'Watermelon']
color= ['red', 'orange', 'yellow', 'green', 'blue']
for f, cin zip(fruit, color):
print('The {0} is {1}'.format(f, c))
The Apple is red
The Orange is orange
The Banana is yellow
The Watermelon is green

===Sorting === pdf slide 61 ====
•Use sort()for simple, in-placesorting:
items = [37, 2, 0, -14]
items.sort()
print(items)# [-14, 0, 2, 37]
•Use sorted()to return a list
–sorted() is ideal for immutable types such as tuples
new_items= sorted(items)  
print(new_items) # [-14, 0, 2, 37]  
  #items can be any iterable
•Using reverse=Trueas an argument will sort from largest to smallest:
	items = [37, -14, 0, 2]
	items.sort(reverse=True)
new_items= sorted(items, reverse=True)print(items, new_items)
	[37, 2, 0, -14] [37, 2, 0, -14]

===Sorting Using a Key
•Specialized sorting can be accomplished using a function (key) that defines what to compare

nums = ['13', '1', '11', '4']
nums.sort()
print(nums)

def sort_func(val):
    return int(val)
nums.sort(key=sort_func)
print(nums)

def sort_func(val):
    return int(val)
nums2 = sorted(nums, key=sort_func)
print(nums2)

===•Lambdas are inline-functions
	–For quick, short, throw away uses such as sorting, closures, functional programming
		funcName= lambda <arguments> : <expression>

	–Can be used anywhere functions are used
	•type() for a lambda returns<type 'function'>

def sort_func(val):
   return int(val) 
..equivalent to...
lambda val: int(val)
---------
•Sorting a list of records by age (descending)
records = [('John', 'Smith', 43, 'jsbrony@yahoo.com'),
           ('Ellen', 'James', 32, 'jamestel@google.com'),
           ('Sally', 'Edwards', 36, 'steclone@yahoo.com'),
           ('Keith', 'Cramer', 29, 'kcramer@sintech.com')
     ]
records.sort(key=lambda one_rec: one_rec[2], reverse=True)
print(records)
[('John', 'Smith', 43, 'jsbrony@yahoo.com'),
('Sally', 'Edwards', 36, 'steclone@yahoo.com'),
('Ellen', 'James', 32, 'jamestel@google.com'),
('Keith', 'Cramer', 29, 'kcramer@sintech.com')]
--------------------------------------
===Copying Lists
•Classic approach uses slicing
a= [ 1, 'hello', ['up', 'down'] ]
b= a[:]   #Makes a shallow copy, doesn't work for all sequence types such as generators, tends to be fastest
•Constructor approach
b = list(a)  #Works with all sequence types, still a shallow copy only

•Deep copy  #Makes a deep copy, slowest in performance
import copy
b = copy.deepcopy(a)
b[2][0] = 'backward'
print(a, b)
	[1, 'hello', ['up', 'down']] [1, 'hello', ['backward', 'down']]

---------------------------------
Task 1-4  
read files from a dir and sort them on size
import glob
import os
#path = input('Path pattern to search: ')        # example: *.py
path='../*'
files = []
files2 = []
dir_items = glob.glob(path)
print(dir_items)
for item in dir_items:
    if os.path.isfile(item):
        files.append(item)
        filesize = os.stat(item).st_size
        filename = os.path.basename(item)
        files2.append((filename, filesize))
#files.sort(key=lambda a: os.stat(a).st_size, reverse=True)
#print(files)
def sort_func(item1):
	return os.stat(item1).st_size
files.sort(key=sort_func,reverse=True)
print(files)

files2.sort(key=lambda rec1:rec1[1])
for item in files2:
    print(' nmae= {}  size= {}'.format(item[0],item[1]))


=================================================================
feb 6   2018 
slide 69 
===List Comprehensions
•List comprehensions provide a Pythonic way to make lists from other lists
–Similar to loops and they take the following form:
newlist= [ expression for varin iterable]
list1 = [1, 2, 3, 4, 5]
list2 = [x*2 for x in list1]
print(list2)   #[2, 4, 6, 8, 10]

newlist= [ expression for varin iterable test_condition]
list1 = [1, 2, 3, 4, 5]
list2 = [x*2 for x in list1 if x % 2 == 0]
print(list2)  #[ 4, 8]

EX:=====Task1-5
import glob
import os
path = '../*'
dir_contents = glob.glob(path)
files = [item for item in dir_contents if os.path.isfile(item)]
files.sort(key=lambda rec1: os.stat(rec1).st_size)
print(files)
files = [(item,os.stat(item).st_size) for item in dir_contents if os.path.isfile(item)]
files.sort(key=lambda rec1: rec1[1])
print(files)

----------------------------------------------
===Named Tuples
•Named tuples are tuples that support names instead of indices
–Similar to but simpler than creating classes
–They are ordered, more readable than dictionaries


from collectionsimport namedtuple  #Import the namedtuple()function from the collections module
Contact= namedtuple('Contact', 'first last age email')
	#Can be a space-separated stringof properties or a list of strings
records = [Contact('John', 'Smith', 43, 'jsbrony@yahoo.com'),
Contact('Ellen', 'James', 32, 'jamestel@google.com'),
Contact('Sally', 'Edwards', 36, 'steclone@yahoo.com'),
Contact('Keith', 'Cramer', 29, 'kcramer@sintech.com'),
]

records.sort(key=lambda one_rec: one_rec.age, reverse=True)
for record in records:
	print(record.last, record.age)

--------
import  collections
person =  collections.namedtuple('personType','name age')
plist=person('sally',35)
print(plist[0])
print(plist.name)
----------------
===Sets
•Sets are collections that disallow duplicate items
–Unordered, iterable, mutable
–Support len(), in, comparisons
–Members must be hashable (immutable) such as int, float, str, tuple
–Disallows list, dict, set, custom objects
–frozensetis an immutable set version
s1 = set([1, 2, 3, 2])
print(len(s1)) # 3
s2 = {4, 5, 6}  
print(s1.isdisjoint(s2)) # True
s3 = frozenset([2, 4, 7])
print(s2.difference(s3)) # {5, 6}
===Set methods
s1.issubset(s2)
s1.issuperset(s2)
s1.isdisjoint(s2)
s1.copy()
s1.add(element)
s1.clear()
s1.remove(element)
s1.intersection(s2)
s1.discard(element)

===Dictionaries
Dictionaries are collections of name/value pairs
	#In other languages we may refer to these as hashes, hashmaps, maps, lookups, tables, etc.
–Unordered, mutable, iterable
–Supports len() and in comparisons
–Keys should be hashable (immutable)
–Values may be anything
	d = { key1 : value1, key2 : value2, ... }
my_dict= {}
my_dict= dict()   #empty dicts
my_dict= { 'item1' : 'value1', 'item2' : 'value2' }
my_dict= dict(item1='value1', item2='value2')

my_dict['item3'] = 'value3'  #adding / changing values
print(my_dict['item2'])     #accessing values

---Accessing Dictionaries
d1 = {'Smith': 43, 'James': 32, 'Edwards': 36, 'Cramer': 29}
•Direct accesscan generate a KeyError
d1['Smith']# returns 43
d1['Green']# generates a KeyError
•Use exception handling to deal with aKeyError
try:
value= d1['Green']# generates a KeyError
except KeyError:
value = 0
•dict.get(key) to retrieve values also:
d1.get('Edwards')# returns 36
d1.get('Green')# returns None
•dict.get(key, default) is safest
d1.get('Cramer', 0)# returns 29
d1.get('Green', 0)# returns 0

---Iterating Over Dictionaries
d1 = {'Smith': 43, 'James': 32, 'Edwards': 36, 'Cramer': 29}
•Iteratinga dictionary directly returns keys:
for item in d1:
	print(item)
Smith
Edwards
James
Cramer

•Iterating a dictionary's values:
for val in d1.values():
print(val)
43
32
29
36

•Accessing both key and value simultaneously:
for key, val in d1.items():
print('Key: {key}, Value: {val}'.format(key=key, val=val), end=' ')
	#items() returns a (view of) list of tuples

d1 = {'Smith': 43, 'James': 32, 'Edwards': 36, 'Cramer': 29}
for item in d1:
	print('key={} val={}'.format(item,d1[item]))
key=Smith val=43
key=James val=32
key=Edwards val=36
key=Cramer val=29

---Other dict methods
d1.copy()
d1.clear()
d1.fromkeys([key_seq])
d1.pop(key, def)
d1.setdefault(key, def)
d1.update(d2)

===Sorted Dictionaries
d1 = {'Smith': 43, 'James': 32, 'Edwards': 36, 'Cramer': 29}
•Dictionaries are unorderedand cannot be sorted
•d1.keys() or d1.values() can be sorted
sorted(d1.keys())   # ['Cramer', 'Edwards', 'James', 'Smith']
sorted(d1.values()) # [29, 32, 36, 43]

•Sorting by keys but returning the values:
list3 = [value for (key, value) in sorted(d1.items())]   #[29, 36, 32, 43]

===Task1-6
In file count the number of occurrences of words & Print top 100 words (5 letters or more) that occur the most

word_dict = {}
for line in open('alice.txt',encoding='utf8'):
    words = line.strip().split()
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

sortedwords = sorted(word_dict.items(),key=lambda rec:rec[1],reverse=True)
print(sortedwords)
five_letter=[(word,count) for word,count in sortedwords if len(word) >= 5]
print(five_letter[:100])
-------
from collections import defaultdict

word_dict = defaultdict(int)
for line in open('alice.txt'):
    words = line.strip().split()
    for word in words:
        word_dict[word] += 1
        # if word in word_dict:
        #     word_dict[word] += 1
        # else:
        #     word_dict[word] = 1

sorted_list = sorted(word_dict.items(), key=lambda one_rec: one_rec[1])
five_letters_or_more = [(key, val) for key, val in sorted_list if len(key) >= 5]

print(five_letters_or_more[-1:-100:-1])


===========Chapter 2 =====================
slide 83
===Exception Handling Structure
•Exceptions are handled using the try -except mechanism
try:
unsafe code
except 	exception1 as e1:
	exception1 handling
except exception2 as e2:
	exception2 handling
else:
	rare to use, perform if
	try block is successful
finally:
	always perform

---Alternate version without except
try:
    unsafe code
finally:
    always perform
-----------
a = input('Number 1: ')
b = input('Number 2: ')
try:
result = float(a) / float(b)
print('Division result is: {0}'.format(result))
except ValueError:
print('Improper value entered.')
---------------
a = input('Number 1: ')
b = input('Number 2: ')
try:
print('Division result is: {0}'.format(float(a) /float(b)))
except ValueError:
	print('Improper value entered.')
except ZeroDivisionError:    #Zero causes ZeroDivisionError, hits the second except block
	print('Number 2 may not be zero.')
-----------
a = input('Number 1: ')
b = input('Number 2: ')
try:
	result = float(a) / float(b)
	print('Division result is: {0}'.format(result))
except (ValueError, ZeroDivisionError):
	print('Improper value entered.')
------------
a = input('Number 1: ')
b = input('Number 2: ')
try:
	result = float(a) / float(b)
	print('Division result is: {0}'.format(result))
except Exception:   #Legal, but as a rule of thumb, try to handle the morespecific exception type and avoid the generic usage shown here
	print('Improper value entered.') 
------------
a = input('Number 1: ')
b = input('Number 2: ')
try:
	result = float(a) / float(b)
	print('Division result is: {0}'.format(result))
except Exception as err:
	print(err, type(err))

=====Working with Files
•Use the built-in open() command to work with files
	-Default mode is 'rt' (read text)
	-We specify the encoding because the default encoding is platform-specific
        -encoding  is new option in  python3
# read text
file = open(filename, encoding='utf8')
# write text
file = open(filename, 'w', encoding='utf8')
mode = 'r' or 'w' or 'r+' or 'a'(read, write, read+write, or append)
f = open('myfile.txt')  # f is a file object
entire_file= f.read()   #String containing entire file contents

f.readline()          # reads one line from a file, retains newline
f.readline(10)        # reads first 10 characters from the line    
list = f.readlines()  # reads all lines, puts them in a list       
f.writelines(list)    # writes a list, one item per line to a file 
-------------
for line in open('myfile.txt', encoding='utf8'):
	process(line)    # line will include the termination character (\n) 
-------------
try:                   
f = open('my_file.txt')    #If file is not found, open() fails, f will be None, therefore close()can't be called, so a nested try-finally structure is required                          
try:                   
	for data in f:         
	# work with data       
finally:               
	f.close()              
except IOError as e:    
  print(e)  

OR
f = None                            
try:                   
	f = open('my_file.txt')
	for data in f:         
		# work with data       
except IOError as e:    
	print(e)               
finally:               
	if f:                  
		f.close()    

•We always want to properly clean up when working with files
–Also true for many other resources, such as: database and network connections, sockets, etc.
•The following is a common programming paradigm:
do some initialization
do some work
do some cleanup

=======•with is a control structure that performs the following:
do some initialization
do work
do some cleanup
–Requires a context manager object to be supplied
withcontextmanageras obj:
do_work
--A context manager is a special object that defines how to initialize at the beginning and clean up afterwards

•The file object can be used in a with control
–It is a context manager because it has an__enter__() and __exit__() method defined
lines = []
try:
    with open('alice.txt') as f:
        lines = f.readlines()
except IOErroras e:
    print('Handled {0}'.format(e)) 
  
print('{0} lines read.'.format(len(lines)))

===Under the Sheets: How 'with' Works
•Context managers are objects that define two methods: __enter__and __exit__
•__enter__is always called at the beginning
–Return value becomes the optional 'as' object
•__exit__is called no matter what happens
class CtxMgr(object):
    def__enter__(self):
        print('enter')
        return 'foo'
    def__exit__(self, typ, value, traceback):
        print('exiting')
        
with CtxMgr() as obj:
    print(obj)
Outputs:
enter
foo
exiting
-------------------
===Multiple Contexts
•Python 3 supports multiple context managers within a single 'with' control:

filename, outfile= 'alice.txt', 'alice_out.txt'
try:
	with open(filename)as f_in, open(outfile, 'w')asf_out:
		for line in f_in:
		  f_out.write(line)
except IOError as e:
	print(e)

with open(outfile) as f:
	print(len(f.readlines()))

===Writing to Text Files
•In write'w' mode, use the file's write()method
–write()accepts a string that should end with \n
–Python will translate \n into a platform-specific line termination character

data = ['Lorem ipsum dolor sit amet, consectetur',...
'qui officiadeseruntmollitanimid estlaborum.',]

try:
  with open('data.txt', 'w', encoding='utf8') as f:
   for line in data:
     f.write('{0}\n'.format(line))
except IOErroras e:
   print(e)



===•Format values according to the user's locale:
import locale
locale.setlocale( locale.LC_ALL, "")
	Sets the locale for to the user’s default setting (typically found in the LANGenvironment variable)

locale.currency( 223471113.18, grouping=True )    # $223,471,113.18


===Print Formatting
•The print function has the following syntax:
print(val1, val2, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
	#sep = String inserted between values
	#end= defines a string appended to the end of the string
	#file= Defines where output will be sent
	#flush= Force flush the stream buffer
	
python 2  
	string is ascii mode 
    
python 3  
   string is unicode based
   print is a full function , should () always
   
-----------------------------------------------
===Task2-1
---•Write a program to find the top 10 baseball salariesfor a specified input year (1985 -2015)
===Logic 1------------------------------------------
import locale
import os.path
from collections import namedtuple

locale.setlocale(locale.LC_ALL, '')
working_dir = '../resources/baseball/'
master_filename = 'Master.csv'
salaries_filename = 'Salaries.csv'
results_filename = 'results.txt'

input_year = 0
salaries = []
players = {}
top_sals = []
SalaryRecord = namedtuple('SalaryRecord','playerid salary  year')
#input_year = input('Enter year (1985 - 2015): ')
input_year = 1985
try:
    with open(os.path.join(working_dir, salaries_filename), encoding='utf8') as f_sal:
        f_sal.readline()  # just read first line of column headings in .csv
        for line in f_sal: # starting to read from 2nd line
            record = line.strip().split(',')
            year, _, _, playerid, salary = record
            if int(year) == input_year :
                try:
                    salaries.append(SalaryRecord(playerid, int(salary), year))
                except ValueError:
                    pass
except IOError as err:
    print('Error   reading salary info '.format(err))
    sys.exit(42)
try:
    with open(os.path.join(working_dir, master_filename), encoding='utf8') as f_mast:
        for line in f_mast:
            record = line.strip().split(',')
            playerid, first, last = record[0], record[13], record[14]
            players[playerid] = (first, last)
except IOError as err:
    print('Error   reading master file  '.format(err))
    sys.exit(42)
salaries.sort(key=lambda record: record.salary, reverse=True)
with open(results_filename, 'w', encoding='utf8') as f_out:
    heading = '{0:30} {1:<20}  {2:<8}'.format('Name', 'salary', 'year')
    print(heading, file=f_out)
    print(heading)
    for record in salaries[:10]:
        playerid = record.playerid
        name = ' '.join(players[playerid])
        salary = locale.currency(record.salary, grouping=True)
        output = '{0:30}  {1:<20} {2:<8}\n'.format(name, salary, record.year)
        print(output, file=f_out)
        print(output)
====Logic 1  end -----------------------------
====Logic 2 -----------------------------------
import locale
import os.path


locale.setlocale(locale.LC_ALL, '')

working_dir = '../../resources/baseball/'
master_filename = 'Master.csv'
salaries_filename = 'Salaries.csv'
results_filename = 'results.txt'

input_year = 0
salaries = []
players = {}
top_sals = []


def salary_sort(sal_record):
    """
        Used for the key= parameter to sort the player-salary data by salary
        :param sal_record: string value representing a players salary
        :return: integer value for the salary
    """
    salary = 0
    try:
        salary = int(sal_record[4])
    except ValueError:
        pass

    return salary

#
#  Step 1.
#  Obtain the user's input, disallow non-int values or an empty selection
#
while True:
    input_year = input('Search salaries for what year?--> ')
    try:
        input_year = int(input_year)
        break
    except ValueError:
        print('Invalid year, try again.')

#
# not a requirement, but this allows option to choose how many records to return
#
num_records = 10
try:
    num_records = int(input('Number of records to retrieve (def.=10): '))
except ValueError:
    print('Retrieving 10 records.')


try:
    # Steps 2 & 3.
    # open and read data from both files
    #
    with open(os.path.join(working_dir, salaries_filename)) as file_sal, \
         open(os.path.join(working_dir, master_filename)) as file_mast:
        for line in file_sal:                                               # get each salary record
            sal_record = line.strip().split(',')
            try:
                record_year = int(sal_record[0])
                if record_year == input_year:
                    salaries.append(sal_record)                                     # load it into a list
            except ValueError:
                pass

        for line in file_mast:                                              # get each player record
            mast_record = line.strip().split(',')
            players[mast_record[0]] = mast_record                           # load it into a list

        # Step 4
        salaries.sort(key=salary_sort, reverse=True)                        # sort the salary records in descending order according to salary

        for top_sal in salaries:
            year = 0
            try:
                year = int(top_sal[0])                                  # get the year for each salary record
            except ValueError:
                pass

            # Step 5.
            playerid = top_sal[3]                                       # get the player's id, salary, year
            salary = top_sal[4]
            player_data = players.get(playerid)                         # get the player's name data from the other file data structure
            if player_data:                                             # checks if the player has data in the players dictionary, if not, we ignore them
                first_name = player_data[13]
                last_name = player_data[14]
                top_sals.append([first_name, last_name, salary, year])  # create a list of the player's relevant data
                if len(top_sals) == num_records:                        # stop after 10 records
                    break
except IOError as e:
    print('Error: {0}'.format(e))


#
#   Step 6. Write the results to a file
#
try:
    with open(results_filename, 'w', encoding='utf8') as f_out:         # write the results to a file
        f_out.write('Results\n')
        f_out.write('{0:<40} {1:<20} {2:<8}\n'.format('Name', 'Salary', 'Year'))
        for player_data in top_sals:
            name = ' '.join(player_data[0:2])
            salary = locale.currency(int(player_data[2]), grouping=True)
            year = player_data[3]
            f_out.write('{0:<40} {1:<20} {2:<8}\n'.format(name, salary, year))
except IOError as e:
    print(e)


# Testing the results
try:
    with open(results_filename) as f_test:                              # read the results back to verify them
        for line in f_test:
            print(line.rstrip())
except IOError as e:
    print(e)
====Logic2 end ---------------------------------------------------
def get_search_year():
    """ obtain the user's input, disallow non-int values or an empty selection"""
    input_year = 1985
    while True:
        input_year = input('Search salaries for what year?--> ')
        try:
            input_year = int(input_year)
            break
        except ValueError:
            print('Invalid year, try again.')

    return input_year

print (get_search_year())
------------
def get_record_count():
    """  Returns number of records to search for """
    num_records = 10
    try:
        num_records = int(input('Number of records to retrieve (def.=10): '))
    except ValueError:
        print('Retrieving 10 records.')

    return num_records
print(get_record_count)
--------------------
 

===Templating Mechanisms
•Templating provide a means for transforming data into 
another format (usually text formats such as HTML, XML, vCard)

import string 
records = [('cow', 'moon'),('dolphin', 'highwire'),('stuntman', 'bus')] 
tmpl= string.Template('The ${animal} jumped over the ${item}.')
for record in records:
	print(tmpl.substitute(animal=record[0], item=record[1]))
	
===•A popular 3rdparty templating tool is Jinja2
		#  Jinja2 supports 2.6, 2.7, 3.3+
from jinja2 import Template
records = [('cow', 'moon'),
('dolphin', 'highwire'),
('stuntman', 'bus')]
tmpl=Template('The {{animal}} jumped over the {{item}}.')
for record in records:
	print(tmpl.render(animal=record[0], item=record[1]))
	
---Jinja2 Scripting
<html>
	<body>
		{% for record in records %}
			<p>The {{record[0]}}jumpedover the {{record[1]}}.</p>
		{% endfor%}
	</body>
</html>
ch02_files_flow_control/templates/example_tmpl.jinja

from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateError, TemplateNotFound
env = Environment(loader=FileSystemLoader('./templates'))


try:
	tmpl= env.get_template('example_tmpl.jinja')
	print(tmpl.render(records=records))
except (TemplateNotFound, TemplateError) as e:	
	print('Error: {0} {1}'.format(type(e), e))

====Installing 3rdParty Tools: pip
•Jinja2 is an external module that must be installed before using it
•Most packages can be installed using a special tool called pip(python package installation tool)
	pip installs into <PYTHON_HOME>/Scripts (on Windows) 
	or the bin directory (on OS X or Linux)
	
•To use pip:
pip install package # pip install Jinja2
python -m pip install package  # another way to run pip	
pip uninstall package
pip3.6 install package  # pip3.6 install Jinja2
Python 3.6 already has pip installed, you may have to create a shortcut/alias for it.

===What Is PyPI?
–PyPiis the Python Package Index Repository
–Contains 3rdparty resources
•Sometimes called the CheeseShop(named after a Monty Python skit)
http://pypi.python.org/pypi
pip search package # pip searchJinja2



===Salaries Rendered as HTML
•Revisiting the baseball exercise--this time output will be an HTML pagerendered using Jinja2
–A Jinja2 HTML template is used to render the table: 
     ch02_file_flow_control/templates/baseball_stats.jinja
try:
	tmpl= env.get_template('baseball_stats.jinja')
	results = tmpl.render(records=top_sals)
	with open(results_filename, 'w', encoding='utf8') as f:
        f.write(results)
except (TemplateError, TemplateNotFound, IOError) as e:
	print('Error: {0}, {1}'.format(type(e), e))
import webbrowser
webbrowser.open(results_filename)

	
    
	
=============7 feb 2018  wednesday=========================

7 feb 2018  wednesday
slide 113 on pdf 
Function Definitions
•Functions provide a means to write reusable code
collections.namedtuple.__doc__  --> give the documentation of namedtuple function
–Python affords powerful features to functions 
deffunc_name(arg0, arg1, arg2, ..., argN):
	statements
	return value
	#Function statements must be indented
	#Return values are optional. A value of 'None' is returned when a return statement is omitted
	#List of parameters must be supplied or () if none


===Calling Functions
•Functions must be defined before they can be called
defdisplay_results(customer, purchase_amount):
	print('Customer: {first} {last}, amount: ${p_amt:,.2f}'.format(first=customer['first'],
			last=customer['last'],
			p_amt=purchase_amount))	
cust= {'first': 'James','last': 'Smith'}
display_results(cust, 1108.23)			

--Using Default Arguments
def convert_file_size(filesize, precision=1, override=None):
	# details of this function are not relevant

print(convert_file_size(12))# 0 KB
print(convert_file_size(1200))# 1.2 KB
print(convert_file_size(1200, 3, 'MB'))# 0.001 MB
print(convert_file_size(12000000000))# 11.2 GB
print(convert_file_size(12000000000, 2, 'TB'))# 0.01 TB
print(convert_file_size(12000000000, 2, 'KB'))# 11,718,750 KB

--Keyword Arguments
•All functions support keyword parameters
–Function calls become more flexible using this technique
def  convert_file_size(filesize, precision=1, override=None):
	# details not shown ...
All of these would be valid calls:
convert_file_size(1200)
convert_file_size(1200, 3, 'MB')
convert_file_size(1200, precision=3, override='MB')
convert_file_size(filesize=1200, precision=3, override='MB')
convert_file_size(precision=3, override='MB',filesize=1200)
convert_file_size(override='MB',filesize=1200)

---Multiple Positional Arguments
•To define a function in which the number of parameters to it are unknown, use the (*) character:
def display_info(name, age, spouse, *children):
	print(name, age, spouse, children)
display_info('Bob', 37, 'Sally', 'Timmy', 'Johnny', 'Annie')
	#Bob 37 Sally ('Timmy', 'Johnny', 'Annie')
	
---Multiple Keyword Arguments
–Results are placed into a dictionary
def display_info(**family):
	print(family)
	
display_info(name='Bob', age=37, spouse='Sally',child1='Timmy',  child2='Johnny', child3='Annie')
  # output = {'child1': 'Timmy', 'child2': 'Johnny', 'child3': 'Annie', 'name': 'Bob', 'age': 37, 'spouse': 'Sally'}

---Mixing Positional and Keywords
def  display_info(*args, **kwargs):
	print(args, kwargs)
display_info('hello', 10, ['stuff1', 'stuff2'],item1='value1', foo='bar')	

	#('hello', 10, ['stuff1', 'stuff2']) {'item1': 'value1', 'foo': 'bar'}
--print()  function is example of using positional and keyword arguments
---Unpacking Arguments
•In a function definition, *and **'collect' values
•These symbols may also be used in the function call
–Values are dispersed, or 'spread out' in the function def
–It works the opposite as it does in the function declaration

def display_results(customer, purchase_amount):
print('Customer: {first} {last}, amount: ${p_amt:,.2f}'
.format(p_amt=purchase_amount, **customer))
		# Customer is a dictionary, so using ** on the dictionary in the function call will cause the dictionary to be 'expanded' into keyword arguments supplied to this function.
cust= {'first': 'James','last': 'Smith'}
display_results(cust, 1108.23)



---Introducing Modules
• Modules are namespaces in Python
– Physically, each .py file represents a module
– Functions, variables, classes declared at the top of a
module can be made available to other modules
– These attributes must be imported before being used
• Most modules of Python's standard library are found in the <PYTHON_HOME>/Lib directory
import <moduleName>
from <moduleName> import <attributes>
from <moduleName> import <attributes> as <alias>

import os
import sys
print(os.environ, sys.path)
• What's in a module?
dir(module_name)   #  Identifies contents of a module
help(module_name)
---Adding Your Own Modules
•Python programs locate modules by looking at the sys.path variable
•To ensure sys.path"sees" your modules, perform one of these:
1.Modify sys.path directly
	sys.path.append('/home/modules')
2.Put your modules in the <PYTHON_HOME>/Lib/site-packages
3.Create an OS-level environment variable called PYTHONPATH
---Variable Scope
•Accessing variables within Python follow the acronym LEGB
global_x= 10
def change_global_x():
	global_x= 20     #You might expect this to change the global_x, but it doesn't
	
change_global_x()
print(global_x)   # 10

•To modifythe global variable use the globalkeyword
global_y= 10
def change_global_y():
	global global_y
	global_y= 20
		
change_global_y()
print(global_y) # 20

•A built-in function calledglobals()returns a dictionary of available global vars
#{'__doc__': None, '__spec__': None, '__builtins__': <module 'builtins' (built-in)>, '__package__': None, '__cached__': None,'x': 10, '__name__': '__main__', '__file__': 'student_files/ch03_functions/06_assigning.py', 'change': <function change at 0x0000000002602400>}
x = 10
def change():
	print(globals())
	globals()['x']= 20
change()
print(x)   # 20

•Immutable values passed to a function are passed by value while mutable values are passed by reference
def change_me(lst, tup, scalar):
	scalar += 
	1lst*= scalar
	tup*= scalar
	print(lst, tup, scalar)  # [1, 2, 3, 1, 2, 3] (4, 5, 6, 4, 5, 6) 2
	
scalar = 1
lst= [1, 2, 3]
tup= (4, 5, 6)
change_me(lst, tup, scalar)
print(lst, tup, scalar)     # [1, 2, 3, 1, 2, 3] (4, 5, 6) 1

--------------------
x1=10
x2=15
def check():
    global x1
    print('in function',x1)
    x1 = 20
    print(globals())
    globals()['x2']=25

check()
print(' in main x1= ',x1,'x2 =',x2)

====================================================================


=============Chapter 4 =====================
slide 133 of pdf
Why Classes?
•Earlier we introduced named tuples
	from collections import namedtuple
	Contact = namedtuple('ContactRecord', 'first last age email')
	c = Contact('John', 'Smith', 43, 'jsbrony@yahoo.com')
•Limitations include:
–Inability to easily modify data: it is effectively a tuple
–Operations on this data are maintained separately
Classes create (instantiate) objects
–Object data not only can be modified, but can use the behaviors (methods) defined in the class

class Contact:
	""" Defines a Contact type """
	def__init__(self, name='', address='', phone='', email='',company='', position=''):
		self.name = name
		self.address = address
		self.phone= phone
		self.email= email
		self.company= company
		self.position= position
		
	def__str__(self):
		return '{0}'.format(self.name)

c = Contact('John Smith', '123 Main St.', '(970)322-9088','jsmith433@yahoo.com', 'Acme Inc.',
'Rubber Hole Engineer')

c.alt_email= 'jsmith433@gmail.com'
print(c.name, c.alt_email)
print(c, type(c))  # John Smith <class '__main__.Contact'>
		
===Constructors
class Contact:
def  __init__(self, name='', address='', phone='', email='',company='', position=''):
	# self must always be defined as the first argument in the constructor
	self.name = name
	self.address = address
	...
c = Contact('John Smith')
#Creating instances executes the constructor

---Adding Methods & the self Parameter
class Contact:
	def__init__(self, name='', address=''):
		self.name = name
		self.address= address
		
	def display_columned(self, nw=20, aw=25):
		return '{0:<{nw}} {1:<{aw}} '.format(self.name,self.address, nw=nw, aw=aw)
		
	def__str__(self):
		return '{0} {1}'.format(self.name, self.address)
	__repr__ = __str__
	
c = Contact('John Smith', '123 Main St.')
print(c.display_columned())
	#Instances may invoke the methods defined in the class, 
	but you should not specify self in the call
	
---Using the Class & Magic Methods
class Contact:
	...(as previously defined)...
from modules.contacts2 import Contact
contact_list= []
try:
	with open('../resources/contacts.dat') as f:
		for line in f:
			contact_data= line.split(' ')
			name, address = contact_data[:2]
			contact_list.append(Contact(name, address)) #Instantiate one contact per record
except IOErroras e:
	print('Error: {0}'.format(e))
print(contact_list) 
#[Bob Green, Sally Smith, John Brown, Ed Parker]  
#Printing the entire list causes a nice output because __repr__ = __str__
	

---Instances Usually Backed by Dictionaries
•Most instances have a __dict__property that allow instances to be accessed using dictnotation
c = Contact('John Smith', '123 Main St.', 
	[{'work':'(970)322-9088', 'home':'(970)455-2390'}],
	'jsmith433@yahoo.com', 'Acme Inc.', 'RubberHammers')
print(c.__dict__['name'])
•Dictionary-backed objects can alternatively use
vars():
c.__dict__ is similar to vars(c)
#When working with namedtuplesas dictionaries, version 3.4.3 and later (as well as 2.7.5 and later) should use _asdict()instead of vars().

---Defining Properties
class Contact:
	def__init__(self, name='', address='', email='', ...):
		self.name= name
		self.address= address
		self.email= email
		...
		
	@property
	def name(self):
		return self._name

	@name.setter
	def  name(self, name):
		self._name= name

#•Properties are Python's version of getters and setters
#Use @property to define a method that can act like a getter
#@prop.setteris the syntax to define a setter
	
	@property
	def email(self):
		return self._email
		
	@email.setter
	def email(self, email):
		if '@' not in email:
			self._email= ''
		else:
			self._email= email
-•The@ syntax describes a decorator
-The "private" property is set in the setter

•Use the properties as if they were typical attributes
–Performing assignments will execute the setter method
	c = Contact()
	c.name= 'Bob'  # Invokes name() setter
	c.email= 'bob@yahoo.com'  #Invokes email() setter
	print(c, c.email)  # Invokes email() getter
-----------------------------------
class player:
    def __init__(self, fname='',lname= ' ',salary =0,playerid=''):
        self.first_name=fname
        self.last_name=lname
        self.salary=salary
        self.playerid=playerid
    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
    @property
    def first_name(self):
         return self._first_name
    @first_name.setter
    def first_name(self,fname):
        self._first_name=fname
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,salary):
        self._salary=0
        if salary > 0:
              self._salary=salary

play1 = player('boby','joseph',3000,10)
print(play1,play1.salary)
	
========================================================
8 feb 2018

Class Attributes
•Variables created at the class level are called class attributes
–They should be modified via the class:

class RaceCar:
	MAX_SPEED = 24
	ACCELERATION = 5
	
	def__init__(self):
		self.speed= 0
		
	def accelerate(self):
		self.speed+= RaceCar.ACCELERATION
		if self.speed> self.MAX_SPEED:
			self.speed= self.MAX_SPEED
#Class attributes can be accessed by both the Class AND the instance, 
but should not be modified by the instance
--Note: do not try to modify ACCELERATION through the instance:
self.ACCELERATION= 10 would be inappropriate

====Static Methods
---Python defines static methods using the @staticmethoddecorator
import urllib.request
from urllib.errorimport URLError

class Page:
	@staticmethod
	def page_load(url):  #Do not specify self , Call is accomplished directly via Classname.methodname()
		try:
			with urllib.request.urlopen(url) as f:
				results = f.read().decode()
		except URLErroras e:
			results = 'Error: {0}'.format(e)
		
		return results
webpage = 'http://cisco.com'
print(Page.page_load(webpage))

====Inheritance: Classic Constructor Call
class Contact:
	def__init__(self, name='', address='', phones=None):
		self.name = name
		self.address= address
		self.phones= phones
	
	def __str__(self):
		return '{name} {address} {phones}'.format(**self.__dict__)
		
class BusinessContact(Contact):
	def __init__(self, name='', address='', phones=None, email='', company='', position=''):
		Contact.__init__(self, name, address, phones)  #Calls the base class constructor
		self.email= email
		self.company= company
		self.position= position
		
positionbc= BusinessContact('John Smith', '123 Main St.',
{'home': '(970)455-2390'})
print(bc)

---Using super() -Preferred
class Contact:
	def__init__(self, name='', address='', phones=None):
		self.name = name
		self.address= address
		self.phones= phones
	
	def__str__(self):
		return '{name} {address} {phones}'.format(**vars(self))

class BusinessContact(Contact):
	def__init__(self, name='', address='', phones=None, 
			email='', company='', position=''):
		super().__init__(name, address, phones)
		self.email= email
		self.company= company
		self.position= position
		
bc= BusinessContact('John Smith', '123 Main St.',{'home': '(970)455-2390'})
print(bc)

==================

*********************************************************************************************
chapter5
=====Introducing the Python Standard Lib
•The Standard Library contains over 200 modules of functions and classes
•Documentation:
	https://docs.python.org
	https://docs.python.org/3/library/index.html

•Use dir()within an interactive shell to view top-level properties of an object or module
>>> dir(sys)
['__displayhook__', '__doc__', '__excepthook__', '__name__', '__package__','__stderr__',
 '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', '_getframe', 'api_version',
 'argv', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats',
 
•The sys module includes resources for monitoring the Python interpreter environment:
sys.path    list of directories the interpreter uses to locate modules
sys.modules dictionary of all loaded modules and their file locations
sys.argv    list of command line arguments starting with the file name
sys.builtin_module_names  tuple of strings identifying all pre-compiled modules (no .pyfile exists for these)
sys.exit(exit_value)   exits the program with an optional exit value
sys.stdin
sys.stdout

sys.stderr    file objects that reference the standard streams
sys.version   gives information about the Python version used
sys.exc_info()  gives type, value, tracebackinforfor a current exception
sys.getrefcount(obj)   number of references to an object (will always be 1 high)

====sys Module Example: A whichModule Utility
import importlib
import sys

defwhichmod(modules):
	for module in modules:
		if module in sys.builtin_module_names:
			print('{module} built in'.format(module=module))
		else:
			try:
				module = importlib.import_module(module)
				location = module.__file__
				print('{loc}'.format(loc=location))
			except (ValueError, ImportError):
				print('{module} not found'.format(module=module))
				
module_names= input('Module name(s) [separated by spaces]: ')
modules = module_names.strip().split(' ')

if len(modules[0]) < 1:
	modules = ['os', 'sys', 'string', 'subprocess',
				'Customers', 'parser', 'foo']
				
whichmod(modules)

==== osModule
•The osmodule provides access to many operating system services

os.name  -string yielding the name of the operating system (e.g. 'nt')
os.environ  -a dictionary of osenvironment variables
os.sep  -path separator character (e.g. semi-colon on windows
os.pathsep -path separator character (e.g. semi-colon on windows ';')
os.linesep -platform specific end of line character (e.g. semi-colon on windows '\r\n')
os.chdir(dir_path)-changes to a specified directory
os.listdir(dir_path)-lists the contents of a particular directory
os.walk(directory)-powerful function that returns directory and file information. 
			It traverses an entire subtree in a directory structure.
os.path  -name of the osspecific module for additional processing. 
		 This module contains many additional functions for working with OS paths.
		 
os.getcwd()	-get the current working directory
os.getenv(envVariable, default) -returns an environment variable
os.rename(old, new)	-rename a file or directory
os.remove(filepath)	-removes a file (errors on directories)	
os.rmdir(path)-remove a directory
os.removedirs(path)-recursively remove all directories
os.chdir(path)-change to a new directory
os.mkdir(dir)-make a directory
os.makedirs(dirs)-make all specified directory levels
os.listdir(path)-return a list of files in a dir
os.path.isfile(file)-checks whether item is a file
os.path.isdir(dir)-checks whether item is a directory
os.path.exists(path)-checks for existence of a file or dir
os.path.basename(path) -returns only the last path level
os.path.join(path1, path2, ....)-smartly joins paths
os.split(path)-returns a head and tail where tail is only the last part of a path
os.walk(path)-walks all files and dirsof a path	 
		 
======os.stat()
import os
import time
stats = os.stat('./os_stat.py')	 #os.stat(filename) -returns statistics on a file or path
print(stats.st_size)
print(stats.st_atime)
print(time.ctime(stats.st_atime))  #Sun Feb 22 19:59:17 2018

print(time.strftime('%m-%d-%Y', time.localtime(stats.st_atime)))
print(stats)

os.stat_result(
st_mode=33206,   #File permissions bits
st_ino=39687971717207165,  # inode
st_dev=2150466117,  #device
st_nlink=1,
st_uid=0,
st_gid=0,
st_size=57,   #filesizein bytes
st_atime=1424652882,  #Last access time, mod time, creation time in secs.
st_mtime=1424652882,
st_ctime=1423761797
)


	 
		 
====time Module
	

====datetimeModule
•The datetimemodule defines a date, time, and datetimeclass for encapsulating specific dates
-date 
year
month
day

-time
hour
minute
second
microsecond
tzinfo

-datetime
year
month
day
hour
minute
second
microsecond
tzinfo

import datetime
now1 = datetime.datetime.now()# current date & time
now2 = datetime.date.today()# current date
print(now1, now2)

d = datetime.date(2009, 1, 1)
print(d.year, d.month, d.day)
print('formatted using strftime: {fmt}'.format(fmt=d.strftime('Day %d of %B, Day %j in %Y, ')))

====csv Module
•The CSV module simplifies working with csv files:
import csv
airports=[]
try:
	with open('../resources/airports.dat', encoding='utf8') as f:
		try:
			for row in csv.reader(f):
				airports.append(row)  #row represents a list of strings from one line within the file
		except csv.Erroras e:
			print('Error: {err}'.format(err=e))
except IOErroras e:
	print(e)
	
try:
	with open('first100.dat', 'w', encoding='utf8') as f:
		try:
			csv.writer(f).writerows(airports[1:101])
		except csv.Erroras e:
			print('Error: {err}'.format(err=e))
except IOErroras e:
	print(e)
	
	






===========chapter 7=======================
Regular  expression
•Python supports Perl-style regex's via the remodule
•Module-level methods include:

match(pattern, string, flags) -from the beginning, return Match object if a match exists, None otherwise
search(pattern, string, flags) -search entire stringfor match, return Match object if exists, None otherwise
findall(pattern, string, flags)-list of matches of patterns within string
finditer(pattern, string, flags)-iterator of matches of patterns in string
fullmatch(pattern, string, flags)-apply pattern to full string, Match object or None returned
split(pattern, string, maxsplit, flags)break string up by regex pattern
sub(pattern, repl, string, count, flags)find match, replace replwith it. Return new string.

•To avoid confusion by having to escape characters within a regex string, use raw strings:
matchobj= re.match('\\d{5}', '12345')
matchobj= re.match(r'\d{5}', '12345') #With raw strings, backslashes are not treated as special character

====Common Regexes
Symbol   Meaning
^	fromthe start
$	to the end
.	any character
\s	whitespace
\S	non-whitespace
\d	digit
\D	non-digit
\w	alphanumeric character
\W	non-alphanumeric character
\b	word boundary
\B	non-word boundary
*	0 or more
+	1 or more
?	0 or 1
{n}	exactly n
{5,8} 5 to 8
{5,}  5 or more
{,8}  Upto 8
(1|2|3)  1or 2or 3
[adrn]   a or d or r or n
[a-f]    oneof a thru f
[^def]   not d or e or f
[a-zA-Z] one of any letter

===Match Objects
•A Match object is returned from either match() or search()

matchobj= re.search('seven', speech)
if matchobj:
	print('seven found at pos: {0}'.format(matchobj.start()))
	
–Match object methods:
start()-index of the start of the match
end()-index of the end of the match
span()-both values (start, end)
groups()returns a tuple of all sub-groups (parenthesized expressions)
group(n)specified sub-group, zero is the whole match

•When a match occurs, matchobj.groups() will return a tuple of the whole match and any subgroups
–Use matchobj.group(n)to obtain the subgroup
matchobj= re.search(r'(\w+) (\w+) (\w+)',
		'Four score and seven years ago')
print(matchobj.groups()) # ('Four', 'score', 'and')
print(matchobj.group(0)) # Four score and
print(matchobj.group(1)) # Four
print(matchobj.group(2)) # score
print(matchobj.group(3)) # and

---Using findall()
•The findall() method allows for finding multiple occurrences of a regex
–Returns a list of strings that match
str_matches= re.findall(r'\w+', 'Four score and seven years ago')
print('How many words: {0}'.format(len(str_matches)))  #How many words: 6
print(str_matches)  #['Four', 'score', 'and', 'seven', 'years', 'ago']

---substitution
import re
word = 'hello-,.?????.\....\..?'
print(word)
#word = re.sub(r'([-,.?]|[??]|[..])','', word) # match symbols patten in [] on word and replace with  ''
#word = re.sub(r'[-\\?.,]{2}','', word.lower())# serach and repalce 2 occrance of symbol in [-\?.:;,!]
word = re.sub(r'[-\\?.,]{2,}','', word.lower())#  repalce 2 or more occrance of symbol in [-\?.:;,!] and replace ''
#word = re.sub(r'([-,.\\?{2,}])','', word)
print(word)
===============================================================
========XML=====================================================

# stats.py (from our task4-1 exercise), this goes in ch04_oo/task4_1/support directory
from collections import namedtuple
import locale
import lxml.etree as etree
from lxml.etree import ElementTree
from lxml.etree import Element
import sys

locale.setlocale(locale.LC_ALL, '')


class Player(object):
    def __init__(self, first, last, salary, year):
        self.first = first
        self.last = last
        self.salary = salary
        self.year = year

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = 0
        if salary > 0:
            self._salary = salary



def get_year():
    """Gets the year from user input"""
    return input('Enter year (1985 - 2015): ')


def retrieve_data(year_input, salaries_filepath, master_filepath, num_records=10):
    players = {}
    salaries = []
    top_sals = []
    SalaryRecord = namedtuple('SalaryRecord', 'playerid salary year')

    try:
        with open(salaries_filepath, encoding='utf8') as f_sal:
            for line in f_sal:
                record = line.strip().split(',')
                year, _, _, playerid, salary = record
                if year == year_input:
                    try:
                        salaries.append(SalaryRecord(playerid, int(salary), year))
                    except ValueError:
                        pass
    except IOError as err:
        print('Error reading salary information: {0}'.format(err))
        sys.exit(42)

    try:
        with open(master_filepath, encoding='utf8') as f_mast:
            for line in f_mast:
                record = line.strip().split(',')
                playerid, first, last = record[0], record[13], record[14]
                players[playerid] = (first, last)
    except IOError as err:
        print('Error reading master file: {0}'.format(err))
        sys.exit(42)

    salaries.sort(key=lambda record: record.salary, reverse=True)

    for record in salaries[:num_records]:
        top_sals.append(Player(players[record.playerid][0], players[record.playerid][1],
                               record.salary, record.year))

    return top_sals


class PrintReportException(Exception):
    def __init__(self, message):
        self.message = message


def print_report(data, columns, results_filename='results.txt'):
    try:
        with open(results_filename, 'w', encoding='utf8') as f_out:
            heading = '{0:30}{1:<20}{2:>12}'.format(*columns)
            print(heading, file=f_out)
            print(heading)

            for player in data:
                name = ' '.join([player.first, player.last])
                salary = locale.currency(player.salary, grouping=True)
                output = '{0:30}{1:<20}{2:>12}'.format(name, salary, player.year)
                print(output, file=f_out)
                print(output)
    except IOError:
        raise PrintReportException('Error writing report!')


def create_xml(data, xml_filename):
    root = Element('players')
    tree = ElementTree(root)

    for record in data:
        player = Element('player')
        first = Element('first_name')
        last = Element('last_name')
        salary = Element('salary')
        player.set('year', record.year)
        first.text = record.first
        last.text = record.last
        salary.text = '${0:,}'.format(record.salary)
        player.append(first)
        player.append(last)
        player.append(salary)
        root.append(player)

    with open(xml_filename, 'w', encoding='utf8') as f_out:
        f_out.write(etree.tostring(root, pretty_print=True).decode())
        print(etree.tostring(root, pretty_print=True).decode())

# task4_1_starter.py (driver), this goes in ch04_oo/task4_1 directory
import os

import ch04_oo.task4_1.support.stats as stats

working_dir = '../../resources/baseball/'
master_filename = 'Master.csv'
salaries_filename = 'Salaries.csv'
results_filename = 'results.txt'

year_input = stats.get_year()

top_sals = stats.retrieve_data(year_input, os.path.join(working_dir, salaries_filename),
                               os.path.join(working_dir, master_filename))

try:
    stats.print_report(top_sals, ['Name', 'Salary', 'Year'], results_filename)
except stats.PrintReportException as err:
    print('An error occurred while writing the report. {0} '.format(err))
stats.create_xml(top_sals, 'results.xml')


==============================================================
chapter 6  Network programming

Humbles, Ashley R.  (coordinator)
Crider, Brad J. , criderbj@wellsfargo.com
Dalal, Saroj S. , saroj.s.dalal@wellsfargo.com
John Crews ,  richard.j.crews@wellsfargo.com
Lifeng Bian  ; lifeng.bian@wellsfargo.com
Mark Feifarek ; mark.feifarek@wellsfargo.com
Otieno, Willys  , willys.otieno@wellsfargo.com  Quantitative Analytics Cons
Sedani, Mayur M.  ,mayur.m.sedani@wellsfargo.com, Technology Manager
Shane Biesemeyer  , shane.biesemeyer@wellsfargo.com
Zhiyu  ; zhiyu.liu@wellsfargo.com
	
Dettler, Derek D., Derek.D.Dettler@wellsfargo.com
Derek.D.Dettler@wellsfargo.com  contact him to setup pyCharm in wellsfargo  laptop
Jim Meek  , james.a.meek@wellsfargo.com
Student Manual:






