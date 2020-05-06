new_name = input()
cats_cnt = 0
max_cnt = 0
max_cafe = ''
while new_name != 'MEOW':
    cats = new_name.split(' ')
    cats_cnt = int(cats[1])
    cats_cafe = cats[0]
    if cats_cnt > max_cnt:
        max_cafe = cats_cafe
        max_cnt = cats_cnt
    new_name = input()
print(max_cafe)