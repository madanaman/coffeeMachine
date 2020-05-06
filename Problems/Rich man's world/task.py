counter = 0
initial_sum = int(input())
while initial_sum <= 700000:
    initial_sum = initial_sum + (initial_sum * 7.1)/100
    counter += 1
print(counter)