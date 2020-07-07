a = []
b = []

class NotPalindromeError(Exception):
    def __init__(self):
        super().__init__('회문이 아닙니다.')
            
def palindrome(word):
    for i in word:
        a.append(i)
    b = a[::-1]
    if b == a:
        return print(word)
    else:
        raise NotPalindromeError()

try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)
