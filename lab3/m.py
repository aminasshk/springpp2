import u
grams = float(input("Enter weight in grams: "))
print(f"In ounces: {u.ounces(grams)}")
num = int(input("Enter a number: "))
if u.is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
