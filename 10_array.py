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
print(language)
value = [5,8,7,9]
value.append(113)
print(value)
value.extend([14,17,19])
print(value)



