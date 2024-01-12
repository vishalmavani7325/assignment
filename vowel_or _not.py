
# 5 Write a Python program to check whether an alphabet is a vowel or consonant.

ch=input("Input a letter of the alphabet: ")
if ch in('a', 'e', 'i', 'o', 'u'):
    print('is a vowel letter ')
else:
    print('is a consonant letter ')
    
    
#6 example string

example = "Favtutor article"

vowels = ["a", "e", "i", "o", "u"]
count = 0

# using for-each loop, character is reference to a letter in the string
for character in example:
    if character in vowels:
        count += 1


print("Number of vowels in the given string is: ", count)