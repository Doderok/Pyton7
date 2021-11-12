def print_till_zero(n):
    if n == 1:
        return n
    else:
        print(n)
        return print_till_zero(n-1)
print(print_till_zero(4))
