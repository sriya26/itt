# initializing string
str = "This;; sentence! has @ a lot'' of punct-!uations..,/"

# printing original string
print("The original string is : " + str)

# initializing punctuations string
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# Removing punctuations in string
# Using loop + punctuation string
for ele in str:
	if ele in punc:
		str = str.replace(ele, "")

# printing result
print("The string after punctuation filter : " + str)


#sort in alphabetical order
alpha=['a','c','d','b','t','g']
print(alpha)
x = sorted(alpha)
print("Alphabetically sorted list: ")
print(x)
