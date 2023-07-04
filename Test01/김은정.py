# 1번
num = input("주민번호를 입력하세요('-'를 입력해주세요).")
if num[7]=='1' or num[7]=='3' or num[7]=='5':
    print ('남성입니다.')
if num[7]=='2' or num[7]=='4' or num[7]=='6':
    print ('여성입니다.')

# 2번
week = input("요일을 입력하세요")
if week =='MON':
    print ('월요일')
if week =='TUE':
    print ('화요일')
if week =='WED':
    print ('수요일')
if week =='TUR':
    print ('목요일')
if week =='FRI':
    print ('금요일')
if week =='SAT':
    print ('토요일')
if week =='SUN':
    print ('일요일')

# 3번
age = input("나이를 입력하세요")
if age < '19':
    print('애들은 가라')
else:
    print('어서오십시오, 손님~!!')

# 4번
filename = './result.txt'
f = open(filename, mode='wt', encoding='utf-8')

n = 1
while (n>=1 and n<=10000):
    if (n % 3 == 0 or n % 5 == 0):
        print(n, file=f)
    n +=1

f.close()
print(f'{filename} 이(가) 생성되었습니다')

# 5번
from datetime import datetime
now = datetime.now()
print(now.strftime('%Y\%m-%d %H*%M%%%S'))
