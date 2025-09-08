t = '-'
s = '.|.'
boy, en = map(int, input().split())
for i in range(boy//2):
    pattern = s * (2*i + 1)  
    line = pattern.center(en, t)
    print(line)