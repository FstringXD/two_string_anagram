from collections import Counter

def are_anagrams(str1, str2):
    # Normalize: remove spaces and make lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return Counter(str1) == Counter(str2)

# Input from user
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Check and print result
if are_anagrams(str1, str2):
    print("✅ The strings are anagrams.")
else:
    print("❌ The strings are NOT anagrams.")
