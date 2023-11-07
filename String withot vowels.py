string = "Welcome to Python Programing"

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""

for char in string:
    if char not in vowels:
        result = result + char

print("After removing Vowels: ", result)