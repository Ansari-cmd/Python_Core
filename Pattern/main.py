# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j > n+1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
        
#     print()

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 10

# #seen = set()
pairs = []

for num in lst:
    complement = k - num
    if complement in lst:
            pairs.append((complement, num))
    #seen.add(num)

print(pairs)

# Example string
# text = "aaffdg^&^77878jhgxfdsfGHG"

# # Initialize an empty dictionary to store character counts
# char_count = {}

# # Loop through each character in the string
# for char in text:
#     # If the character is already in the dictionary, increment its count
#     if char in char_count:
#         char_count[char] += 1
#     # If the character is not in the dictionary, add it with count 1
#     else:
#         char_count[char] = 1

# # Print the character counts
# for char, count in char_count.items():
#     print(f"'{char}': {count}")

# a = "hjhjghgheh"
# out={}
# for i in a:
#     if i  not in out:
#         out[i] = 1
#     else:
#         out[i] += 1
# print(out)


# a = "asasd"
# out={}
# i = 0
# while i < len(a):
#     if a[i] not in out:
#         out[a[i]] = 1
#     else:
#         out[a[i]] += 1
#     i+=1
# print(out)