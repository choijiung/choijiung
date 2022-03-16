#리스트: 순서를 가지는 객체의 집합

#지하철 칸별로 10명, 20명, 30명

#subway = 10
#subway2 = 10
#subway3 = 30

subway = [10, 20, 30]# 리스트
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호가 몇번째에 있는기 알기
print(subway.index("조세호")+1)

#하하가 다음 정류장에 탔다
subway.append("하하")
print(subway)

#정현돈은 유재석과 조세호 사이에 넣기
subway.insert(1, '정형돈')
print(subway)

#뒤에서부터 한명씩 꺼내기
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

#같은 사람이 몇명이 있는지 확인
subway.append('유재석')
print(subway)
print(subway.count('유재석'))

#정렬
num_list = [5,6,4,8,10,9,7,2,3,1]
num_list.sort()
print(num_list)

#순서 뒤집기 가능
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형과 같이 사용
num_list = [5,6,4,8,10,9,7,2,3,1]
mixlist = ["Hello",1,"apple",3.14]
print(mixlist)

#리스트 확장
num_list.extend(mixlist)
print(num_list)