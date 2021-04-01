import requests

# URL -> Uniform Resource Locator
# 자원이 위치한 경로
# 프로토콜://도메인:포트번호/경로
# 프로토콜: 자원이 위치한 경로로 접근할 때 어떤 방법으로 접근할 것인지
# 도메인: 자원이 위치한 인터넷 주소
#       : 0~255 3자리의 한 묶음을 4개로 묶어서 표현한 것
# 포트번호: 해당 자원으로 접속하기 위한 포트번호 (0~65, 535번) (80, 433번 일반적으로 열어둠?)
# 경로: 해당 자원이 위치한 추가적인 경로
url = 'https://www.naver.com'

response = requests.get(url)
# status_code : 상태코드(주로 200(성공), 400(요청 오류), 500번대 사용)
print("응답코드 : {}".format(response.status_code))
print(response.text)







