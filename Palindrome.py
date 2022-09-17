#Name:Harshal Patel
#SID: 28994291
#Date: Sept - 16 - 2022
#Program: Palindrome
#Description: Checks the input array for a palindrome, and returns a yes if there is one.

words = ["Computer","dad","is ","aswesome","we","love","it","here"]


# isPalindrome checks if there is even 1 word that is a palindrome and if so it outputs true.
def isPalindrome(words):
	for x in words:
		if(x==x[::-1]):
			return True
            
# printResult checks what the result is and prints an output accordingly
def printResult(result):
    if result:
        print("Yes, there is a palindrome in the list of words given!")
    else:
        print("No palindromes found in the list of words.")       

result = isPalindrome(words)
printResult(result)


