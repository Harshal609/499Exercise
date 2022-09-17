#Name:Harshal Patel
#SID: 28994291
#Date: Sept - 16 - 2022
#Program: Palindrome
#Description: Checks the input array for a palindrome, and returns a yes if there is one.

words = ["Computer","science","is ","aswesome","we","love","it","here"]
result = False

# isPalindrome checks if there is even 1 word that is a palindrome and if so it outputs true.
def isPalindrome(words):
    i = 0
    while(result):
        word = words[i]
        if (word == word[::-1]):
            result = True
        i += 1

# printResult checks what the result is and prints an output accordingly
def printResult(result):
    if result:
        print("Yes, there is a palindrome in the list of words given!")
    else:
        print("No palindromes found in the list of words.")       





