def mul(a,b):
    if a < b:
        return mul(b,a)
    elif b != 0 :
        return (a + mul(a, b-1))
    else:
        return 0
print(mul(2,3))