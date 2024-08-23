import sys
sys.setrecursionlimit(5000)
sys.set_int_max_str_digits(999999)
def fact1(n):
    if n == 0:
        return 1
    else:
        return n*fact1(n-1)
    
print(fact1(2000))
