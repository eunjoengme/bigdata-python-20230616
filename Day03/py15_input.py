# 입출력
import datetime # 날짜를 모듈 가져움

birth_year = int(input('출생년도를 입력하세요 > ')) # 키보드 입력(무조건 str)int()로 형변환 필요

print(f'당신의 출생년도는 {birth_year}년 입니다') # 콘솔출력
curr_year = datetime.datetime.now().year # yyyy-MM-dd hh:mm:ss.ms
#print(curr_year)
age = curr_year - birth_year
print(f'당신의 나이는 {age}세 입니다')


print(range(10))
print(len(range(10)))

for i in range(20):
    if i == (len(range(20))-1):
    print(i, end=' ')
    