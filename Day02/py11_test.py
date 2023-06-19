# Q1
l1 = { '국어' : 80,
    '영어' : 75,
    '수학' : 55}

print(l1.values())

sum = 0
for item in l1.values():
    sum += item
print(f'홍길동의 평균점수는{sum/3} 입니다.')

# Q2 1)
x =13
a = x % 2
type(a)
if[ a==1 ]:
    print('홀수')
else:
    print('짝수')

# Q2 2)
number = 13
result = 13 % 2 == 0
print(f'{number}는 짝수? {result}')

# Q3
pin = "881120-1068234"
yyyymmdd = pin[0:6] # yyyymmdd = pin.split('-')[0]
num = pin[7:14]     # num = pin.split('-')[1]
print(yyyymmdd)
print(num)

# Q4
print(pin[7])

# Q5
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

# Q6
a = [1,3,5,4,2]
a.sort()
print(a)
a.reverse()
print(a)

a = [1,1,1,2,2,3,3,3,4,4,5]
print(set(a))
