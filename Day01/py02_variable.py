# 변수
import sys

number = 10
value = sys.maxsize + 1 # sys.maxsize 파이썬 시스템에서 제공하는 최고숫자

print(number)
print(value + 1)

value2 = 0o12 # 8진수
print(value2)

value2 = 0xFF 
print(value2)

value2 = 'Hello, python'
print(value2)

value2 = False
print(value2 == False)

# 사칙연산, 수학식
print(14 / 2) # 소수점 나누기
print(14 // 2) # 정수로 나누기
print(2 ** 10) # 승수 2의 10승
print(10 % 3) # 나머지(3의 배수 결과값=0)