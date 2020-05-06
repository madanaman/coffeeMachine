# i = int(input())
# while i < 100:
#     if i > 10:
#         print(i)
#     i = int(input())
# while True:
#     i = int(input())
#     if i > 100:
#         break
#
#     elif i > 10:
#         print(i)

ip = input()
itr = len(ip) // 2
pal_bool = "Palindrome"
for i in range(itr):
    if ip[i] != ip[len(ip)-i-1]:
        pal_bool = "Not palindrome"
        break
print(pal_bool)