vowel=("a","e","i","o","u")
str=input("enter string")
str1=" "
for letter in str:
    if letter not in vowel:
        str1+=letter
        
print(str1)
