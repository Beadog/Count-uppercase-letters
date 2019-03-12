'''
Corrie Stewart
Program counts number of uppercase letters in a string entered by user
Date: 11/4/18
'''

def main():
    s = input("Enter a string: ")
    print("The number of uppercase letters in the string is", countUppercase(s))

def countUppercase(s):
    high = len(s) - 1
    return countUppercaseHelper(s, high)

def countUppercaseHelper(s, high):
    count = 0
    if high >= 0:
        count = countUppercaseHelper(s, high - 1) + (1 if s[high].isupper() else 0)
    return count

main()
