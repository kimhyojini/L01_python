# 복습
# 다양한 자료를 이용하여, 정보를 구조화하는 방식이 알고리즘에서 중요하다.

# 복습 실습 
users = {
        'total_user': 3,
        'information': [
            {'name': 'alex', 'age':3, 'license':True},
            {'name': 'june', 'age':7, 'license':False},
            {'name': 'peter', 'age':4, 'license':False}
        ]
        }

# 구조 확인
print(type(users))
print(users.keys()) # 키-값의 한쌍 구조로 만들어진, 순서가 없는 컨테이너 자료형

print(users['total_user']) # int
print(users['information']) # list -> 순서가 존재하는 컨테이너 자료형

# 사람들의 정보만 뽑아보기
infos = users['information'] # 리스트만 뽑아서 할당
print(infos[0]) # 순서가 존재하기 때문에 숫자(위치)로 값 접근

# Q1. 라이센스가 있는 인원들의 숫자 구하기
# => 라이센스 == True 인 사람의 수 (세기)
cnt = 0 # 초기값

print('Q1.')
for info in infos:
    if info['license'] == True:
        cnt += 1

print(f'라이센스가 있는 인원 {cnt} 명')

# Q2. 모든 사람의 나이 평균 구하기

# Q3. 라이센스가 없는 사람들의 이름 모으기