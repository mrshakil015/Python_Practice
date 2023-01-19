import array
language = ["C","C++","Java","Python"]
print("Accessing elements: ",language[1])
print("Accessing elements: ",language[-1])
print("Length of the array: ",len(language))

#Adding elements to an array
language = ["C","C++","Java","Python"]
language.append("Javascript")
print(language)
language.insert(2,"React Native")
print("Add elements at the specific index: ",language)
value = [5,8,7,9]
value.append(113)
print("Add elements at the end: ",value)
value.extend([14,17,19])
print("Add elements at the end: ",value)


#Removing elements of an array
print("Array: ",language)
print("Popping last element: ",language.pop())
print("Popping 2nd element: ",language.pop(1))
language.remove("Java")
print("After popping and removing array is: ",language)