
print("\nMany values to Multiple variables")
x,y,z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


print("\nOne values to Multiple variables")
x=y=z = "Orange"
print(x)
print(y)
print(z)

print("\nUnpack a collection")
fruits = ["apple", "banana", "cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)

#You can also use the + operator to output multiple variables:
x= "Python "
y= "is "
z= "interesting"

print(x+y+z)
