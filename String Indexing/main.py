# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"
print(credit_number[3]) #4
print(credit_number[:4]) #1234
print(credit_number[5:9])  #5678
print(credit_number[5:])  #5678-9012-3456
print(credit_number[::3]) #146-136

# negetive indexing

print(credit_number[-1]) # 6
print(credit_number[::-1]) # reverse 6543-2109-8765-4321


last_digit = credit_number[-4:] #3456

print(f"XXXX-XXXX-XXXX-{last_digit}")