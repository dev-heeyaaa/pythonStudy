import requests

url = ''
param_dic = {}

fullURL = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=파이썬'
fullURL = fullURL.split("?")

url = fullURL[0]
parameter = fullURL[1]

parameter = parameter.split("&")

for param in parameter:
    param = param.split("=")
    print(param)

    param_dic.setdefault(param[0], param[1])

print(url)
print(parameter)

print(param_dic)

# URL에서 ? 뒤에 오는 것들은 파라미터(Parameter)
# 자원이 사용할 재료
# 파라미터는 이름=값 으로 구성되어있음
# 이름과 값은 & 기호를 사용해서 구분을 한다
# https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=파이썬

response = requests.get(url, param_dic)

print("응답 코드 = {}".format(response.status_code))
print(response.text)

