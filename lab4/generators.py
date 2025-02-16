#1
def square_generator(n):
    for i in range(n + 1):
        yield i ** 2
n=int(input())
for square in square_generator(n):
    print(square, end=" ")

#2
def even_generator(n):
    for i in range(0, n + 1, 2):
        yield i
n=int(input())
print(",".join(str(num) for num in even_generator(n)))

#3
def div_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n=int(input())
print(list(div_by_3_and_4(n)))

#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
a=int(input("Enter A: "))
b=int(input("Enter B: "))
for sq in squares(a, b):
    print(sq)

#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input())
for num in countdown(n):
    print(num, end=" ")
