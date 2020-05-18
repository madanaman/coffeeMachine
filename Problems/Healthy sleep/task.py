min_sleep = int(input())
max_sleep = int(input())
actual_sleep = int(input())

if actual_sleep < min_sleep:
    print('Deficiency')
elif actual_sleep > max_sleep:
    print("Excess")
else:
    print("Normal")
