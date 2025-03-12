# for loop = execute a block of code a fixed number of times.
#            You can iterate over a range, string, sequence, etc

for x in range(1,11,2):
    print(x)
print("HAPPY NEW YEAR")

credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x)

for x in range(1,21):
    if x == 13:
        continue   # skip the current iteration
    else:
        print(x)

for x in range(1,21):
    if x == 13:
        break    # break the entire loop 
    else:
        print(x)
