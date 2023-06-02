import sys
#import subprocess

def printname():
    name = sys.argv[1]
    print("hello",sys.argv[1])
    print("hello variable", name)
    print("hello format {}".format(name))
    print(f"hello fstring {name}")

def argument(lang):
    if lang == 'es':
        print('Hola')
    if lang == 'fr':
        print('Bonjour')

def trycatch(ast):
    try:
        print("in try")
        ast = int(ast)
        print("wont print")
    except:
        ast = 1
    print("Done: ast is",ast)

def retunfun(argu):
    return "Hello",argu #returns a list

def argu(a,b):
    added = a+b
    return added
printname()
argument('fr')
trycatch('bob')
print(retunfun('shreya'))
print(type(retunfun('shreya')))
x = argu(5,7)
print(x)


#loops
def breaksta():
    while True:
        line = input('>')
        if line.casefold() == 'done':
            break
        print(line)
    print('Done')

breaksta()

def conti():
    while True:
        line = input('>')
        if line == "#":
            continue # with continue the iterator goes up and starts the loop again  
        if line == 'done':
            break
        print(line)
    print("Done with continue")
conti()

def forloop():
    for i in range(10):
        print(i)

forloop()

def logicfor():
    largest_so_far = -1
    print('Before Computation, ', largest_so_far)
    for i in [1,64,76,33,25,96,36,7,6,69]:
        if i > largest_so_far:
            largest_so_far = i
        print(largest_so_far)
    print("After, ", largest_so_far)

    zork = 0
    for i in [9,24,41,19,77,89]:
        zork = zork + i
        print(zork, i)
    
    zork = 0
    for i in [9,24,41,19,77,89]:
        zork = zork + 1
        print(zork, i)
    
    found = False
    print("Before found was", found)
    for i in [11,34,56,71,76,84,86,92,97]:
        if i == 86:
            found = True
        print(found, i)
    print("After found is", found)

logicfor()
def findsmallest():
    smallest = None
    for small in [5,17,28,34,39,40,-2,4,7,-9,20,-22]:
        if smallest == None:
            smallest = small
        elif small < smallest:
            smallest = small
        
    print("Smallest nummer in list", smallest) 

findsmallest()

def letter(lett):
    fruit = lett
    for i in range(len(fruit)):
        letter = fruit[i]
        print(letter)
    
    for i in range(len(fruit)):
        letter = fruit[i-1]
        print(letter)
    index = 0
    while index < len(lett):
        letter = fruit[index]
        print(index, letter)
        index = index+1

    for i in range(5, 40, 2):
        print(i)
    for l in fruit:
        print(l)
    count = 0
    for l in fruit:
        if l == "o":
            count = count + 1
    print("number of o's", count)
letter('broccoli')

def slicingStrings(slice11):
    print(slice11[0:4])
    print(slice11[6:7])
    print(slice11[6:20])
    print(slice11[:2])
    print(slice11[8:])
    print(slice11[:])

    
    vowel=0
    for i in slice11:
        if i in ['a','e','i','o','u']:
            vowel = vowel + 1
    print("numeber of vowels: ",vowel)

    for i in slice11:
        if i in ['a','e','i','o','u']:
            print("vowel found", i)

    print(dir(slice11)) #printing builtin function fo string

    print(slice11.capitalize())
    print(slice11.find('on'))

slicingStrings('dragonfruit')

def replac(name):
    greet = "Hello "+name
    print(greet)
    bye = greet.replace('Hello', 'Bye')
    print(bye)

replac("Shreya")

def stripp():
    x = "   Hi, whats up?   "
    print(x)
    y = x.rstrip()
    print(y)
    z = y.lstrip()
    print(z)
    k = z.startswith("Hi") #print true or false
    print(k)
    m = z.find(',') # prints position
    positionplus = z[m:9]
    print(m)
    print(positionplus)


stripp()

# files
def files():
    testfile = open('password_generator.py', 'r')
    count = 0
    for line in testfile:
        print(line)
        count = count + 1
    print(count)

    # reading file in one go
    data = testfile.read()
    print(len(data))
    print(data[:2])
    
    # to find something in a file
    for line1 in testfile:
        if line1.startswith("if __name__"):
            print(line)

    # removing extra \n as print adds extar \n after every line
    for line2 in testfile:
        line2  = line2.rstrip()
        print(line)
    
    for line3 in testfile:
        print(line3.rstrip())

    for line4 in testfile:
        if not line4.startswith("if __name__"):
            continue
        print()
files()

#def linuxcommand():

 #   version = subprocess.run(['python3', '--version'], capture_output=True, text=True)
  #  pyversion = version.stdout()
  #  versionnumber = pyversion.split(' ')
  #  nums = versionnumber[1].split('.')
  #  number = str(nums[0]+nums[1])

# lists
def listexamples():
    friends = ["one", "two", "three"]
    x = [1,[2,3], 4]
    y = []
    z = list()
    #Lists are mutable
    a = [1,4,7,9,44,66,87]
    a[3] = 8
    lenghta = len(a)
    print(range(len(a)))

    for i in range(len(friends)):
        friend = friends[i]
        print(friend)

    print(a[1:4])
    z.append("hello")
    z.append("Hola")

    b = 'Shreya' in friends
    print(b)
    c = 'four' not in friends

    a.sort()
    print(max(a))
    abc = "Hello Shreya Bhardwaj"
    stuff = abc.split()
    print(stuff)
    bcs = "One;two;ka;four"
    fun = bcs.split(';')
    print(fun)

listexamples()

def scrapping():
    testfile = open('testfile.txt','r')
    for line in testfile:
        line = line.rstrip()
        if not line.startswith('From'):
            continue
        words = line.split()
        if words.__contains__('@'):
            print(words)

scrapping()