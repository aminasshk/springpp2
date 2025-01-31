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

