def decimaltoBinary(n):
    if n > 1:
        decimaltoBinary(n//2)
    print(n % 2,end = '')
dec = 8
decimaltoBinary(dec)
print()