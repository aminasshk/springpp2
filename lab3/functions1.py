#1
def ounces(grams):
    return grams / 28.3495231
grams=float(input())
print(ounces(grams))

#2
def tocelcius(f):
    return (5/9) * (f-32)
f=float(input())
print(tocelcius(f))

#3
def solve(numheads,numlegs):
    for chickens in range(numheads+1):
        rabbits=numheads-chickens
        if 2*chickens+4*rabbits==numlegs:
            return chickens,rabbits
    return "No solution"
numheads=int(input())
numlegs=int(input())
s=solve(numheads,numlegs)
print("Chickens:",s[0])
print("Rabits:",s[1])

#4
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def filter_prime(numbers):
    return list(filter(is_prime, numbers))
numbers_str = input("enter list numbers: ")
numbers_list = list(map(int, numbers_str.split()))
prime_numbers = filter_prime(numbers_list)
print("Prime numbers:", prime_numbers)

#5
def permutations(some):
    n = len(some)
    for i in range(n):
        for j in range(n):
            print(some[(j-i)], end=" ")
        print()
k=str(input("soz:"))
permutations(k)

#6
def _reverse(strings):
    strings=list(strings.split())
    strings.reverse()
    for i in strings:
        print(i, end=" ")
k=str(input("soz:"))
_reverse(k)

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
has_33([1, 3, 3])
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

#8
def order007(arr):
    result = []
    for i in arr:
        if i==0 or i==7:
            result.append(i)
    flag =  False
    for i in range(len(result)-2):
        if result[i]==result[i+1] and result[i]==0 and result[i+2]==7:
            flag = True    
    if flag:
        print("True")
    else:
        print("False")
order007([1,2,4,0,0,5,7])
order007([1,0,2,4,0,5,7])
order007([1,7,2,0,4,5,0])

#9
import math
def volumespher(radius):
    V=(4*math.pi*(radius**3))/3
    return V
radius=float(input("radius:"))
print(volumespher(radius))

#10
def unique(mylist):
    result = []
    for i in mylist:
        if mylist.count(i) == 1:
            result.append(i)
    return result
n = int(input("n: "))
mylist = []
for i in range(n):
    number = int(input("number: "))
    mylist.append(number)
print(unique(mylist))

#11
def palindrom(text):
    if text==text[::-1]:
        print("YES")
    else:
        print("NO")
text = input("text: ")
palindrom(text)

#12
def histogram(arr):
    for i in arr:
        print("*"*i)
n=input("numbers:")
mylist=list(map(int,n.split()))
histogram(mylist)

#13
from random import randint
def guessanumber():
    print("Hello! What is your name?")
    name = input("name:")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = randint(1,20)
    sum = 0
    run = True
    while run:
        guess = int(input("Take a guess: "))
        sum+=1
        if guess == number:
            run = False
            print(f"Good job, {name}! You guessed my number in {sum} guesses!")
            break
        if guess>number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low")
guessanumber()

