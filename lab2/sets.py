#1
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
#2
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
#1
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
#2
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
#3
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
#1
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#2
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
#3
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
#4
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
#5
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
#6
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
#7
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)
print(z)
#1
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#2
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#3
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
#4
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)