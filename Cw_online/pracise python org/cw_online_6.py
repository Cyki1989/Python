'''
def checkPalidrome(word):
    start=0; end=len(word)-1
    while start<end:
        if word[start]!=word[end]:
            isPalidrome=False
            break
        start+=1; end-=1
    else:
         isPalidrome=True
    return isPalidrome

word=input('give me a string to check if it is a palindrome: ')
print(checkPalidrome(word))
'''

'''
def checkPalidrome(word):
    start=0; end=len(word)-1
    while start<end:
        if word[start]!=word[end]:
            isPalidrome=False
            break
        start+=1; end-=1
    else:
         isPalidrome=True
    return isPalidrome

while True:
    try:
        word=input('Give me a string to check if it is a palindrome: ')
        if word.isspace() or not word:
            raise Exception
        break
    except Exception:
        print('Give me at least one character')

print(checkPalidrome(word.strip()))
'''

'''
word=input('give me a string to check if it is a palindrome: ')
revWord=word[::-1]
if revWord==word:
    print('Word "%s" is a palindrome'%word)
else:
    print('Word "%s" is not a palindrome'%word)
'''
