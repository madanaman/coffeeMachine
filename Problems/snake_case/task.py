ip_text = input()
snake_case = ""

for i in ip_text:
    if i.isupper():
        snake_case = snake_case + "_"
    snake_case = snake_case + i.lower()

print(snake_case)
