# Determines whether the string is a palindrome
def is_palindrome(str):
	reverse = str[::-1]
	return True if str == reverse else False

print(is_palindrome("RooR"))
print(is_palindrome("RotoR"))
print(is_palindrome("RostoR"))