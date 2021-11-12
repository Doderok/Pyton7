def is_palindrome(s,i=0):
    if i >= len(s)//2:
        return 'This is a palindrome'
    if s[i] != s[-(i+1)]:
        return 'This is not a palindrome'
    return is_palindrome(s, i+1)

print(is_palindrome(str(input("Введите строку "))))