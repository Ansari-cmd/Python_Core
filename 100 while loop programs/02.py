# First 10 Odd numbers 

count=1
num = 0
while count<=10:
    if num % 2 != 0:
        count+=1
        print(num)
        #print(f"{num}",end=" ")
        
    num+=1